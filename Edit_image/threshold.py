import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 读取图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)

# 全局阈值处理
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)#大于127的像素值设置为255，小于127的像素值设置为0
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)#大于127的像素值设置为0，小于127的像素值设置为255
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)#大于127的像素值设置为127，小于127的像素值保持不变
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)#大于127的像素值保持不变，小于127的像素值设置为0
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)#大于127的像素值设置为0，小于127的像素值保持不变

# 定义标题和图像列表
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

# 创建窗口显示结果
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()



# 读取图像并应用中值模糊
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)
img = cv.medianBlur(img, 5)

# 全局阈值
ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)#大于127的像素值设置为255，小于127的像素值设置为0

# 自适应均值阈值
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)#11表示邻域大小，2表示从均值中减去的常数

# 自适应高斯阈值
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)#11表示邻域大小，2表示从均值中减去的常数

# 定义标题和图像列表
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

# 创建窗口显示结果
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# 读取带噪声的图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)

# 全局阈值
ret1, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Otsu阈值
ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# 经过高斯滤波的 Otsu 阈值
blur = cv.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# 定义标题和图像列表
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)', 'Original Noisy Image', 'Histogram', "Otsu's Thresholding", 'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

# 创建窗口显示结果
for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()

# 读取带噪声的图像并应用高斯模糊
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)
blur = cv.GaussianBlur(img, (5, 5), 0)

# 找到归一化直方图和累计分布函数
hist = cv.calcHist([blur], [0], None, [256], [0, 256])
hist_norm = hist.ravel() / hist.max()
Q = hist_norm.cumsum()
bins = np.arange(256)
fn_min = np.inf
thresh = -1
for i in range(1, 256):
    p1, p2 = np.hsplit(hist_norm, [i])  # 概率
    q1, q2 = Q[i], Q[255] - Q[i]  # 类别总和
    if q1 > 0 and q2 > 0:  # 检查q1和q2是否为零
        b1, b2 = np.hsplit(bins, [i])  # 权重
        m1, m2 = np.sum(p1 * b1) / q1, np.sum(p2 * b2) / q2  # 均值
        v1, v2 = np.sum(((b1 - m1) ** 2) * p1) / q1, np.sum(((b2 - m2) ** 2) * p2) / q2  # 方差
        fn = v1 * q1 + v2 * q2  # 计算最小函数
        if fn < fn_min:
            fn_min = fn
            thresh = i

# 使用OpenCV函数的Otsu阈值
ret, otsu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print("{} {}".format(thresh, ret))