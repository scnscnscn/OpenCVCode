import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
    # 读取每一帧
    _, frame = cap.read()

    # 将BGR图像转换为HSV图像
    # Hue（色调）：表示颜色的种类，例如红色、绿色、蓝色等。范围通常是0到360度（在OpenCV中是0到179）。
    # Saturation（饱和度）：表示颜色的纯度，值越高颜色越鲜艳，值越低颜色越接近灰色。范围是0到255。
    # Value（亮度）表示颜色的明暗程度，值越高颜色越亮，值越低颜色越暗。范围是0到255。
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 定义HSV中蓝色的范围
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([145,255,255])

    # 对原始图像和掩模进行按位与操作，输出的是掩模中的蓝色区域
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 显示原始帧、掩模和结果图像
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
