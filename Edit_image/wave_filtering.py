import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")

# 均值滤波
kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)

# 高斯模糊
blur = cv.GaussianBlur(img,(5,5),0)

# 中值滤波
median = cv.medianBlur(img,5)

# 双边滤波
double_blur = cv.bilateralFilter(img,9,75,75)

# 显示结果
titles = ['Original', 'Averaging', 'Gaussian Blur', 'Median Blur', 'Bilateral Filter']
images = [img, dst, blur, median, double_blur]

plt.figure(figsize=(12, 8))
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

