import numpy as np
import cv2 as cv


img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)
# 二值化后再寻找轮廓，然后选择一个轮廓进行分析
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# 1. 矩 (Moments)
M = cv.moments(cnt)
print("矩:", M)
cx = int(M['m10'] / M['m00'])  # 计算质心
cy = int(M['m01'] / M['m00'])
print("质心:","(", cx, cy," )")

# 2. 轮廓面积
area = cv.contourArea(cnt)
print("轮廓面积:", area)

# 3. 轮廓周长
perimeter = cv.arcLength(cnt, True)
print("轮廓周长:", perimeter)

# 4. 轮廓近似（多边形近似）
epsilon = 0.1 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
print("轮廓近似:", approx)

# 5. 凸包
hull = cv.convexHull(cnt)
print("凸包:", hull)

# 6. 检查凸度（检查轮廓是否为凸多边形）
is_convex = cv.isContourConvex(cnt)
print("检查凸度:", is_convex)

# 7. 边界矩形
# 7.a. 直角矩形
x, y, w, h = cv.boundingRect(cnt)
print("直角矩形:", (x, y, w, h))

# 7.b. 旋转矩形
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int32(box)
print("旋转矩形:", box)

# 8. 最小外圆
(x, y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
print("最小外圆:", center, radius)

# 9. 拟合椭圆
ellipse = cv.fitEllipse(cnt)
print("拟合椭圆:", ellipse)

# 10. 拟合线
[vx, vy, x0, y0] = cv.fitLine(cnt, cv.DIST_L2, 0, 0.01, 0.01)
print("拟合线:", (vx, vy, x0, y0))