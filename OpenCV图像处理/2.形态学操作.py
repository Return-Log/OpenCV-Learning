import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from cv2.cv2 import imread

"""腐蚀和膨胀"""
# img = cv.imread("text.jpeg")
# # 创建核结构
# kenel = np.ones((5,5),np.uint8)
# # 腐蚀
# img2 = cv.erode(img,kenel)
# plt.imshow(img2[:,:,::-1])
# plt.show()
# # 膨胀
# img1 = cv.dilate(img,kenel)
# plt.imshow(img1[:,:,::-1])
# plt.show()

"""开闭运算"""
# open = imread("open.jpeg")
# close = imread("text.jpeg")
#
# kenel = np.ones((3,3),np.uint8)
#
# cvopen = cv.morphologyEx(open,cv.MORPH_OPEN,kenel)
# cvclose = cv.morphologyEx(close,cv.MORPH_CLOSE,kenel)
#
# plt.imshow(cvclose[:,:,::-1])
# plt.show()

"""礼帽和黑帽"""
open = imread("open.jpeg")
close = imread("text.jpeg")

kenel = np.ones((3,3),np.uint8)

top = cv.morphologyEx(open,cv.MORPH_TOPHAT,kenel)
black = cv.morphologyEx(close,cv.MORPH_BLACKHAT,kenel)

plt.imshow(black[:,:,::-1])
plt.show()