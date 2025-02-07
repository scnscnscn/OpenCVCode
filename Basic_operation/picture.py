import numpy as np
import cv2 as cv

# 用灰度模式加载图像
img = cv.imread('lenna_color.png.png', 0)

#直接加载彩色图像
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()

#先创建一个窗口，之后再加载图像
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite('lenna.png',img)

