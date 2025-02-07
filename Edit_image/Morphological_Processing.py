import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('1.png')

# 模糊处理
blur = cv.blur(img, (5, 5))

# 定义膨胀操作的内核
kernel = np.ones((5, 5), np.uint8)

# 膨胀处理
dilation = cv.dilate(img, kernel, iterations=1)

# 开运算（先腐蚀后膨胀）
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# 闭运算（先膨胀后腐蚀）
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

# 形态学梯度（膨胀图像减去腐蚀图像）
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# 礼帽（原始图像减去开运算图像）
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)

# 显示原始图像、模糊处理后的图像、膨胀处理后的图像、开运算后的图像、闭运算后的图像、形态学梯度图像和礼帽图像
plt.figure(figsize=(12, 10))
plt.subplot(241), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(242), plt.imshow(cv.cvtColor(blur, cv.COLOR_BGR2RGB)), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.subplot(243), plt.imshow(cv.cvtColor(dilation, cv.COLOR_BGR2RGB)), plt.title('Dilated')
plt.xticks([]), plt.yticks([])
plt.subplot(244), plt.imshow(cv.cvtColor(opening, cv.COLOR_BGR2RGB)), plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.subplot(245), plt.imshow(cv.cvtColor(closing, cv.COLOR_BGR2RGB)), plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.subplot(246), plt.imshow(cv.cvtColor(gradient, cv.COLOR_BGR2RGB)), plt.title('Gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(247), plt.imshow(cv.cvtColor(tophat, cv.COLOR_BGR2RGB)), plt.title('Tophat')
plt.xticks([]), plt.yticks([])
plt.show()