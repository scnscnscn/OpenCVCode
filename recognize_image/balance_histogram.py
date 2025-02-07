import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# 读取灰度图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)

# 计算直方图和累积分布函数
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()

# 归一化累积分布函数
cdf_normalized = cdf * float(hist.max()) / cdf.max()

# 直方图均衡化
#具体的操作是将输入图像的灰度直方图变成均匀分布的形式，从而增强图像的对比度。
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]

# 读取另一张图像并进行直方图均衡化
#直方图均衡化的实现方法是将输入图像的灰度值作为均衡化的变换函数，从而得到均衡化后的图像。
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Edit_image/1.png", 0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))  # 将图像并排堆叠
cv.imwrite('res.png', res)

# 使用CLAHE进行自适应直方图均衡化
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_gray.jpeg", 0)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
cv.imwrite('clahe_2.jpg', cl1)

# 绘制累积分布函数和直方图
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()