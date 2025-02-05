import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""图像缩放"""
kids = cv.imread("img.png")
# # 绝对尺寸
# rows, cols = kids.shape[:2]
# print(f"{rows},{cols}")
# # res = cv.resize(kids, (1*rows, 2*cols))
# res = cv.resize(kids, (1920, 1080))
# rows1, cols1 = res.shape[:2]
# print(f"{rows1},{cols1}")
# plt.imshow(res[:,:,::-1])
# plt.show()
# # 相对尺寸
# resl = cv.resize(kids,None,fx=1,fy=2)
# plt.imshow(resl[:,:,::-1])
# plt.show()

"""图像平移"""
rows, cols = kids.shape[:2]
# M = np.float32([[1,0,100],[0,1,50]])
# res2 = cv.warpAffine(kids,M,(cols,rows))
# plt.imshow(res2[:,:,::-1])
# plt.show()

"""图像旋转"""
# M = cv.getRotationMatrix2D((cols/2,rows/2),45,0.5)
# res3 = cv.warpAffine(kids,M,(cols,rows))
# plt.imshow(res3[:,:,::-1])
# plt.show()

"""仿射变换"""
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[30,60],[128,65],[45,135]])
M = cv.getAffineTransform(pts1,pts2)
res4 = cv.warpAffine(kids,M,(cols,rows))
plt.imshow(res4[:,:,::-1])
plt.show()