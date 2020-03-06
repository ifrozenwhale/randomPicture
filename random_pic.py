from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from PIL import Image
import random

import matplotlib.patches as patches
from matplotlib.path import Path
import cv2
import numpy as np



def get_random_data(border,number=500,xd=5,yd=5):
    """
    得到有边界限制的随机数据点集
    并且做出随机点图
    :param border: 数据边界，n*2的数组
    :param number: 随机点的数目
    :param xd: 图像的长度指数（一般1-10）
    :param yd: 图像的宽度指数（一般1-10）
    :return: 生成的随机点的坐标
    """

    # 得到 path 数据
    pth = Path(border, closed=False)
    plt.figure(figsize=(xd, yd))
    plt.title('scatter border')
    ax = plt.gca()
    ax = ax.invert_yaxis()
    plt.scatter(pth.vertices[:,0],pth.vertices[:,1], color='#00C5CD')
    plt.savefig('img/random.png',dpi=600)
    plt.show()
    # 得到边界的坐标最值
    min_x = np.min(border[:, 0])
    min_y = np.min(border[:, 1])
    max_x = np.max(border[:, 0])
    max_y = np.max(border[:, 1])

    # 初始化坐标
    pos = np.zeros((number, 2))
    for i in pos:
        while True: # 当随机生成的点不在有界区域内，重新生成
            x = random.randint(min_x, max_x)
            y = random.randint(min_y, max_y)
            i[0] = x
            i[1] = y
            # 判断点是否在有界区域内
            mask = pth.contains_point(i)
            if mask: # 如果在，结束
                break

    return pos

def get_axis_border(pos):
    """
    得到坐标轴的界限
    :param pos: 数据
    :return: [min_x, max_x, min_y, max_y]
    """
    max_x = np.max(pos[:, 0]) * 1.0
    min_x = np.min(pos[:, 0]) / 1.2
    min_y = np.min(pos[:, 1]) / 1.2
    max_y = np.max(pos[:, 1]) * 1.1
    return [min_x, max_x, min_y, max_y]

def calVoronoi(pos,xd=10,yd=5,type=2,name='voronoi',color='#008B8B',linewidth=1,alpha=0.5):
    """
    计算Voronoi，并绘制voronoi图
    :param pos: 随机坐标集
    :param xd: 图像的长（1-10）
    :param yd: 图像的宽（1-10）
    :param type: 默认为2，表示一般的图像。1的处理更加细致，对于图像的要求也更高，要求边界清晰，简洁。
    :param name: 图表标题和保存的文件名
    :param color: 线条颜色
    :param linewidth: 线条宽度
    :param alpha: 线条的颜色透明度
    :return:
    """
    print("In voronoi ")
    # 得到随机数据
    get_random_data(pos,2)
    # 计算Voronoi图
    vor = Voronoi(pos)

    # 设置可以显示中文标题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    # 得到坐标轴范围并进行设置
    axis_border = get_axis_border(pos)
    plt.axis(axis_border)
    # 设置图片尺寸（长宽比）
    fig, ax = plt.subplots(figsize=(xd,yd))
    # Voronoi图绘制
    fig = voronoi_plot_2d(vor, ax, show_vertices=False, line_colors=color,
                          line_width=linewidth, line_alpha=0.8, point_size=0)
    # y轴翻转，以符合原始图像
    ax.invert_yaxis()
    # 不显示坐标轴
    plt.axis('off')
    plt.title(name)
    # 保存的位置
    plt.savefig('img/voronoi' + name + '.png', dpi=800)
    plt.show()


def get_border_list(path):
    """
    得到边界的list
    :param path:
    :return:
    """
    arr = get_border(path,2)
    length = 0
    for i in arr:
        length += len(arr[0])
    print(length)
    data = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            data.append([arr[i][j][0][0], arr[i][j][0][1]])

    return data


def get_border_array(path='img/hua.jpg',type=2):
    """
    得到边界的 array
    :param path: 图片相对路径
    :param type: 图片类型，1表示极简边界图，2表示一般的图（简笔画）
    :return: 边界数组
    """
    arr = get_border(path, type)
    # 计算点数
    length = 0
    for i in range(len(arr)):
        length += len(arr[i])
        print(len(arr[i]))
    print(length)
    x = np.zeros(length)
    y = np.zeros(length)
    arr = get_border(path)
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            x[cnt] = arr[i][j][0][0]
            y[cnt] = arr[i][j][0][1]
            cnt += 1
    # vstack就是垂直叠加组合形成一个新的数组，T是转置
    xycrop = np.vstack((x, y)).T
    return xycrop


def get_border(path='img/hua.jpg',type=2):
    """
    边缘检查，得到边界数据
    :param path: 图片路径
    :param type: 图片类型，1表示极简边界图，2表示一般的图（简笔画）
    :return:
    """
    img = cv2.imread(path)  # a black objects on white image is better
    thresh = cv2.Canny(img, 128, 256)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img = np.zeros(img.shape, dtype=np.uint8)
    cv2.drawContours(img, contours, -1, (255, 0, 0), 2)  # blue
    min_side_len = img.shape[0] / 32  # 多边形边长的最小值 the minimum side length of polygon
    min_poly_len = img.shape[0] / 16  # 多边形周长的最小值 the minimum round length of polygon
    min_side_num = 3  # 多边形边数的最小值
    min_area = 30.0  # 多边形面积的最小值
    approxs = [cv2.approxPolyDP(cnt, min_side_len, True) for cnt in contours]  # 以最小边长为限制画出多边形
    approxs = [approx for approx in approxs if cv2.arcLength(approx, True) > min_poly_len]  # 筛选出周长大于 min_poly_len 的多边形
    approxs = [approx for approx in approxs if len(approx) > min_side_num]  # 筛选出边长数大于 min_side_num 的多边形
    approxs = [approx for approx in approxs if cv2.contourArea(approx) > min_area]  # 筛选出面积大于 min_area_num 的多边形

    if type == 1:
        return contours
    else:
        return approxs


def plot_border(path='img/whale2.jpg'):
    """
    绘制边界图
    :param path:
    :return:
    """
    data = get_border_list(path)
    # print(data)
    x = []
    y = []
    for i in data:
        x.append(i[0])
        y.append(i[1])
    plt.scatter(x, y)
    ax = plt.gca()
    ax = ax.invert_yaxis()
    plt.show()

def get_size(path):
    """
    封装得到图像的长宽比
    :param path: 图片相对路径
    :return: [zoom_length, zoom_width]
    """
    img = Image.open(path)
    size = img.size
    zoom = size[0] / 5
    return [size[0] / zoom, size[1] / zoom]
if __name__ == '__main__':
    # 图片路径
    path = 'img/tree.jpg'
    # 绘制边界
    plot_border(path)
    # 图片的长宽比
    size = get_size(path)
    # 得到边界
    border = get_border_array(path,2)
    # 得到随机数
    data = get_random_data(border,4000)
    # 绘制Voronoi图
    calVoronoi(data, size[0], size[1], name='运动鞋',color='#2F4F4F',linewidth=0.4)