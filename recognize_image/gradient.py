import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)

# 拉普拉斯算子
laplacian = cv.Laplacian(img, cv.CV_64F)

# Sobel算子，x方向求梯度
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)

# Sobel算子，y方向求梯度
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

# Sobel算子，输出类型为cv.CV_8U
sobelx8u = cv.Sobel(img, cv.CV_8U, 1, 0, ksize=5)

# Sobel算子，输出类型为cv.CV_64F，然后取绝对值并转换为cv.CV_8U
sobelx64f = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

# cv.CV_64F
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 2), plt.imshow(sobelx8u, cmap='gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1, 3, 3), plt.imshow(sobel_8u, cmap='gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()

# 黑白过渡为正斜率（有正值），而白黑过渡为负斜率（有负值）。
# 所以当数据转换成 np.uint8 时，所有的负斜率都变成零。简单来说，你失去了边缘。
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()