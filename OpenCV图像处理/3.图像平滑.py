import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""噪声滤波"""
dogsp = cv.imread("jiao.jpeg")
doggau = cv.imread("gao.jpeg")

# # 均值滤波
# dog = cv.blur(dogsp, (5,5))
# plt.imshow(dog[:,:,::-1])
# plt.show()

# # 高斯滤波
# dog1 = cv.GaussianBlur(doggau,(3,3),1)
# plt.imshow(dog1[:,:,::-1])
# plt.show()

# 中值滤波
dog2 = cv.medianBlur(dogsp,3)
plt.imshow(dog2[:,:,::-1])
plt.show()
