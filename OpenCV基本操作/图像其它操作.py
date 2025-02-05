import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""修改图像中像素点"""
img = np.zeros((256, 256, 3), np.uint8)
plt.imshow(img[:,:,::-1])
# plt.show()

print(img[100,100])

print(img[100,100,0])  # 像素点B通道深度

img[100,100] = (0,255,0)

print(img[100,100,1])

"""显示图像属性"""
print(f"**{img.shape};{img.dtype};{img.size}")

"""图像通道拆分与合并"""
gpl = cv.imread("1.png")
# plt.imshow(gpl[:,:,::-1])
# plt.show()
b,g,r = cv.split(gpl)
print(b.shape)
# plt.imshow(b, cmap='gray')
# plt.show()
gpl2 = cv.merge((g,b,r))

"""色彩通道转换"""
gray = cv.cvtColor(gpl, cv.COLOR_BGR2GRAY)
# plt.imshow(gray, cmap='gray')
# plt.show()

hsv = cv.cvtColor(gpl, cv.COLOR_BGR2HSV)
plt.imshow(hsv)
plt.show()