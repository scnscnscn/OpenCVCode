import numpy as np
import cv2 as cv

img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")

# 转换为灰度图像，并二值化
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)

# 寻找轮廓，countours是一个列表，其中每个元素都是一个轮廓，hierarchy是轮廓的层次结构
# cv.CHAIN_APPROX_NONE 是一种轮廓近似方法，它会存储轮廓上所有边界点的坐标。
# cv.CHAIN_APPROX_SIMPLE 是一种更高效的轮廓近似方法。它会删除所有冗余点，并尽可能地压缩轮廓，从而减少存储的点的数量。
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# 绘制所有轮廓
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
# 绘制特定轮廓
cv.drawContours(img, contours, 3, (0, 255, 0), 3)
# 绘制第4个轮廓
cnt = contours[4]
cv.drawContours(img, [cnt], 0, (0, 255, 0), 3)

# 显示图像
cv.imshow('Contours', img)
cv.waitKey(0)
cv.destroyAllWindows()