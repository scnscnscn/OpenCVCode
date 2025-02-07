import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")

# 计算灰度图像的直方图
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hist = cv.calcHist([gray_img], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

# 计算并绘制 BGR 通道的直方图
color = ('b', 'g', 'r')
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])

# 显示直方图
plt.show()