import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1. 图像缩放
# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")
# 使用双三次插值放大图像2倍,INTER_CUBIC表示双三次插值,fx和fy分别表示水平和垂直方向的缩放因子,none表示输出图像的尺寸
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
# 或者直接指定目标尺寸
height, width = img.shape[:2]
res2 = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)

# 创建窗口显示原始图像和缩放后的图像
cv.imshow("Original Image", img)
cv.imshow("Resized Image (fx=2, fy=2)", res)
cv.imshow("Resized Image (2*width, 2*height)", res2)

# 2. 图像平移
# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")
# 获取图像的行数和列数
rows, cols = img.shape[:2]
# M = np.float32([[1, 0, tx], [0, 1, ty]])，tx和ty分别表示水平和垂直方向的平移量
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 应用平移矩阵
dst = cv.warpAffine(img, M, (cols, rows))

# 创建窗口显示平移后的图像
cv.imshow("Translated Image", dst)

# 3. 图像旋转
# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)  # 以灰度模式读取图像
rows, cols = img.shape
# 定义旋转矩阵，将图像绕中心点旋转90度，缩放比例为1
#getRotationMatrix2D(center, angle, scale)函数中center表示旋转中心，angle表示旋转角度，scale表示缩放比例
M = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

# 创建窗口显示旋转后的图像
cv.imshow("Rotated Image", dst)

# 4. 仿射变换
# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")
rows, cols, ch = img.shape
# 定义原始图像中的三个点
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
# 定义目标图像中的对应点
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# 计算仿射变换矩阵
M = cv.getAffineTransform(pts1, pts2)
# 应用仿射变换
dst = cv.warpAffine(img, M, (cols, rows))

# 使用matplotlib显示原始图像和变换后的图像
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Input')
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title('Output')
plt.show()

# 5. 透视变换
#透视变换的特点
#直线保持直线：在透视变换中，原始图像中的直线在变换后的图像中仍然是直线。
#四点对应：需要在原始图像和目标图像中各指定四个点，这四个点对应起来，用于计算变换矩阵。
#三点不共线：在指定的四个点中，任意三个点不能共线，否则无法唯一确定一个透视变换。
# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")
rows, cols, ch = img.shape
# 定义原始图像中的四个点
pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
# 定义目标图像中的四个点
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
# 计算透视变换矩阵
M = cv.getPerspectiveTransform(pts1, pts2)
# 应用透视变换
dst = cv.warpPerspective(img, M, (300, 300))

# 使用matplotlib显示原始图像和变换后的图像
plt.figure(figsize=(10, 5))
plt.subplot(121), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Input')
plt.subplot(122), plt.imshow(cv.cvtColor(dst, cv.COLOR_BGR2RGB)), plt.title('Output')
plt.show()

# 等待用户按键并关闭所有窗口
cv.waitKey(0)
cv.destroyAllWindows()