import numpy as np
import cv2 as cv

e1 = cv.getTickCount()
# 加载图像
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")

# 获取图像的高、宽和通道数
h, w, c = img.shape
print(f"图像的高度: {h}, 宽度: {w}, 通道数: {c}")

# 访问像素值
# OpenCV 中像素值的顺序是 BGR，而不是 RGB
pixel = img[100, 100]  # 获取 (100, 100) 位置的像素值
print(f"位置 (100, 100) 的像素值: {pixel}")

# 修改像素值
img[100, 100] = [255, 255, 255]  # 将 (100, 100) 位置的像素值修改为白色
print(f"修改后的像素值: {img[100, 100]}")

# 使用更高效的方法访问和修改像素值
# 访问红色通道的值
red_value = img.item(10, 10, 2)  # 获取 (10, 10) 位置的红色通道值
print(f"位置 (10, 10) 的红色通道值: {red_value}")

# 修改红色通道的值
img.itemset((10, 10, 2), 100)  # 将 (10, 10) 位置的红色通道值修改为 100
print(f"修改后的红色通道值: {img.item(10, 10, 2)}")
# 获取图像的形状
print(f"图像的形状: {img.shape}")

# 获取图像的总像素数
print(f"图像的总像素数: {img.size}")

# 获取图像的数据类型
print(f"图像的数据类型: {img.dtype}")
# 假设我们有一个图像，我们想提取其中的球并将其复制到另一个位置
# 提取球的区域
ball = img[280:340, 330:390]  # 提取图像中 (280, 330) 到 (340, 390) 的区域
# 将球复制到另一个位置
img[273:333, 100:160] = ball  # 将球复制到 (273, 100) 到 (333, 160) 的区域
# 拆分图像通道
b, g, r = cv.split(img)  # 将图像拆分为蓝色、绿色和红色通道

# 合并图像通道
img_merged = cv.merge((b, g, r))  # 将通道重新合并为一个图像

# 使用 Numpy 索引更快地修改通道
img[:, :, 2] = 0  # 将所有红色通道的值设置为 0
cv.imshow("image", img)
 
e2 = cv.getTickCount()
time = (e2 - e1)/cv.getTickFrequency()
print(f"运行时间: {time} 秒")
cv.waitKey(0)


