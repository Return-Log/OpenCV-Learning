import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""sobel算子"""
img = cv.imread("gao.jpeg",0)
# x = cv.Sobel(img,cv.CV_16S,1,0, ksize = -1)
# y = cv.Sobel(img,cv.CV_16S,0,1, ksize = -1)
# absx = cv.convertScaleAbs(x)
# absy = cv.convertScaleAbs(y)
# res = cv.addWeighted(absx,0.5,absy,0.5,0)
# plt.imshow(res,cmap = plt.cm.gray)
# plt.show()

"""Laplacia"""
# res = cv.Laplacian(img,cv.CV_16S)
# res = cv.convertScaleAbs(res)
# plt.imshow(res,cmap = plt.cm.gray)
# plt.show()

"""canny"""
res = cv.Canny(img,0,100)
plt.imshow(res,cmap=plt.cm.gray)
plt.show()