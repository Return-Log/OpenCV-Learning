import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""绘制直方图"""
img = cv.imread("gao.jpeg", 0)
# hist = cv.calcHist([img],[0],None,[256],[0,256])
# plt.figure(figsize=(10,8))
# plt.plot(hist)
# plt.show()

"""掩膜的应用"""
# # 创建掩膜
# mask = np.zeros(img.shape[:2],np.uint8)
# mask[100:120,20:30] = 1
# mask_img = cv.bitwise_and(img,img,mask=mask)
# mask_hist = cv.calcHist([img],[0],mask,[256],[0,256])
# plt.plot(mask_hist)
# plt.show()

"""直方图均衡化"""
# dst = cv.equalizeHist(img)
# plt.imshow(dst,plt.cm.gray)
# plt.show()

"""自适应直方图均衡化"""
cl = cv.createCLAHE(2.0,(8,8))
clahe= cl.apply(img)
plt.imshow(clahe,cmap=plt.cm.gray)
plt.show()