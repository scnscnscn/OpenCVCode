import cv2 as cv
import numpy as np

A = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png")  # 彩色图像
B = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_gray.jpeg")  # 灰度图像

# 高斯金字塔
G = A.copy()  # 原始图像A作为最底层
gpA = [G]  # 初始化高斯金字塔列表，将原始图像添加进去
for i in range(6):
    # cv.pyrDown()函数降低图像分辨率
    G = cv.pyrDown(G)
    gpA.append(G)

# 高斯金字塔
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# 拉普拉斯金字塔
lpA = [gpA[5]]  # 初始化拉普拉斯金字塔列表
for i in range(5, 0, -1):  # 从倒数第二层向上遍历
    GE = cv.pyrUp(gpA[i])  # cv.pyrUp()函数将当前层图像分辨率提升一倍
    L = cv.subtract(gpA[i-1], GE)  # 计算当前层与上一层扩展后的差异，得到拉普拉斯层
    lpA.append(L)  # 将拉普拉斯层添加到拉普拉斯金字塔列表中

# 拉普拉斯金字塔
lpB = [gpB[5]]  # 初始化拉普拉斯金字塔列表
for i in range(5, 0, -1):   # 从倒数第二层向上遍历
    GE = cv.pyrUp(gpB[i])  # cv.pyrUp()函数将当前层图像分辨率提升一倍
    L = cv.subtract(gpB[i-1], GE)  # 计算当前层与上一层扩展后的差异，得到拉普拉斯层
    lpB.append(L)  # 将拉普拉斯层添加到拉普拉斯金字塔列表中

# 在每个级别上添加图像的左半部分和右半部分
LS = []  # 初始化混合后的拉普拉斯金字塔列表
for la, lb in zip(lpA, lpB):  # 遍历A和B的拉普拉斯金字塔
    rows, cols, dpt = la.shape  # 获取当前层图像的尺寸
    ls = np.hstack((la[:, :cols//2], lb[:, cols//2:]))  # 将A的左半部分和B的右半部分水平堆叠
    LS.append(ls)  # 将混合后的图像添加到混合拉普拉斯金字塔列表中

# 现在重建
ls_ = LS[0]  # 从混合拉普拉斯金字塔的最底层开始
for i in range(1, 6):  # 逐层向上重建
    ls_ = cv.pyrUp(ls_)  # 使用cv.pyrUp()函数提升分辨率
    ls_ = cv.add(ls_, LS[i])  # 将当前层与上一层的混合图像相加

# 直接连接每半部分的图像
real = np.hstack((A[:, :cols//2], B[:, cols//2:]))  # 直接将A的左半部分和B的右半部分水平堆叠

# 显示结果
cv.imshow("Pyramid_blending2", ls_)  # 显示通过金字塔混合后的图像
cv.imshow("Direct_blending", real)  # 显示直接拼接的图像
cv.waitKey(0)  # 等待用户按键