import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 读取图像并转换为灰度
img = cv.imread("C:/Users/WLQVi/Desktop/python/OpenCV/Basic_operation/lenna_color.png", 0)

# 使用 Numpy 进行傅里叶变换
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)  # 将零频率分量移到中心
magnitude_spectrum = 20 * np.log(np.abs(fshift))  # 计算幅度谱

# 显示原始图像和幅度谱
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# 创建高通滤波器 (HPF) 并进行逆傅里叶变换
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
fshift[crow - 30:crow + 31, ccol - 30:ccol + 31] = 0  # 遮罩低频区域
f_ishift = np.fft.ifftshift(fshift)  # 反向移位
img_back = np.fft.ifft2(f_ishift)  # 逆傅里叶变换
img_back = np.real(img_back)  # 取实部

# 显示高通滤波后的图像
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_back, cmap='gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_back)
plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
plt.show()

# 使用 OpenCV 进行傅里叶变换
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)  # 将零频率分量移到中心
magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))  # 计算幅度谱

# 显示原始图像和幅度谱
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# 创建低通滤波器 (LPF) 并进行逆傅里叶变换
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1  # 创建低通滤波器
fshift = dft_shift * mask  # 应用滤波器
f_ishift = np.fft.ifftshift(fshift)  # 反向移位
img_back = cv.idft(f_ishift)  # 逆傅里叶变换
img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])  # 计算幅度

# 显示低通滤波后的图像
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Image after LPF'), plt.xticks([]), plt.yticks([])
plt.show()