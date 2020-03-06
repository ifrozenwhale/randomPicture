# 基于Voronoi图的自定义轮廓内的随机纹路生成

github：https://github.com/FrozenWhalePP/randomPicture

## 总览

### Voronoi图

- Voronoi图又称泰森多边形或者Dirichlet图，由一组由连接两邻点直线的垂直平分线组成的连续多边形组成。具体特点见百度百科。
  https://baike.baidu.com/item/%E6%B3%B0%E6%A3%AE%E5%A4%9A%E8%BE%B9%E5%BD%A2/3428661?fromtitle=voronoi&fromid=9089406&fr=aladdin
- 基于`python`实现，`scipy.spatial.Voronoi`

### 图像边缘检测

- 检测一张图片主题元素的轮廓边界，并提取边界坐标
- 基于`python`的`opencv-python`中的`cv2.findContours()`实现

## 程序文件

### `random_pic.py`

- 给出一张图片，得到图片中主要元素的边界轮廓。
- 产生N个随机数，使得落在边界内部。
- 根据产生的点，绘制Voronoi图
- 可调整参数：
  - 根据图片是否足够简洁确定边界的精度
  - 随机点的数目
  - 绘制的图形线条颜色，宽度，透明度
  - 图形的长宽比，尺寸等

### `random_pic_color.py`

- 在`random_pic.py`的基础上，重写了Voronoi图的绘制函数（参考Stack Overflow上的回答）
- 去线条，使用彩色填充
- 可选参数：
  - 如上
  - 填充颜色的透明度

## 注意

- 图片的边缘检测，轮廓提取算法参考的他人博客，目前精度还有待提升。如果图片元素过多，线条复杂，则效果不佳。建议使用简笔画。
- `random_pic_color.py`目前存在一定BUG，导致KeyValue错误，但是不稳定，失败/成功比例大概为3/1。

## 展示

### 线条

- 冰冻鲸鱼

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi鲸鱼.png" width=75%/>

- 运动鞋

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi运动鞋.png" width=75%/>

- 红色高跟鞋

  <img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi高跟鞋.png" width=75%/>

- 小王子中的蛇吞象

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi蛇吞象.png" width=75%/>

- 橘色的花瓶

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi花瓶.png" width=75%/>

- 冰冷的铁塔

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi艾菲尔铁塔.png"/>

- 迟到的圣诞树

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/voronoi圣诞树.png" width=75%/>

### 色块填充

- 运动鞋

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/color_运动鞋.png" width=75%/>

- 不一样的埃菲尔铁塔

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/color_艾菲尔铁塔.png" width=75%/>

- 奇怪的帽子

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/color_帽子.png" width=75%/>

- 彩色高跟鞋

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/color_鞋子.png" width=75%/>

- 彩色鲸鱼

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/color_whale.png" width=75%/>

- 丑丑的圣诞树

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/color_圣诞树.png" width=75%/>

### 改变随机点个数
- 鲸鱼

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/鲸鱼.jpg" width="75%"/>

- 稀疏裂纹圆

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/圆.jpg" width=75%/>

- 密圆

<img src="https://frozenwhale.oss-cn-beijing.aliyuncs.com/img/圆2.jpg.png" width=75%/>