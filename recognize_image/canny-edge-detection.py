import cv2 as cv
import numpy as np
#cany边缘检测:
# 1.首先进行高斯滤波减少噪声
# 2.水平和垂直方向上用 Sobel 内核对平滑后的图像进行滤波，以获得水平方向（G_x）和垂直方向（G_y）的一阶导数
# 3.Canny 采用非极大值抑制来消除边界检测带来的杂散响应.
# 当前像素的梯度幅度是其邻域中的局部最大值，则保留该像素；否则，将该像素的梯度幅度置为0
#4.滞后阈值：确定边缘的最小值和最大值
#如果像素的梯度幅度大于maxVal，则该像素被认为是“确定边缘”。
#如果像素的梯度幅度小于minVal，则该像素被认为是“非边缘”，并被丢弃。
#如果像素的梯度幅度在minVal和maxVal之间，则根据其连通性来判断是否为边缘：


#canny(src, machVal, minVal, aperture_size=3, L2gradient=False)
#src:输入图像,maxVal:边缘检测的最大值,minVal:边缘检测的最小值,aperture_size:Sobel算子的大小,L2gradient:是否使用L2范数
#关于参数选择：
#黄金比例：maxVal ≈ 3×minVal （比如100和300）
#L2gradient：True用欧式距离更精确，False用曼哈顿距离更快
#aperture_size：Sobel核大小，3/5/7奇数可选，越大越抗噪但也越模糊
#L2gradient=True时，aperture_size只能为3，因为sobel算子是3x3的
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png",0)
# 滑动条回调函数
def nothing(x): pass

cv.namedWindow('Canny')
cv.createTrackbar('MinVal', 'Canny', 0, 500, nothing)
cv.createTrackbar('MaxVal', 'Canny', 0, 500, nothing)

while (1):
    min_val = cv.getTrackbarPos('MinVal', 'Canny')
    max_val = cv.getTrackbarPos('MaxVal', 'Canny')

    edges = cv.Canny(img, min_val, max_val, L2gradient=True)

    cv.imshow('Canny', np.hstack([img, edges]))
    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()
