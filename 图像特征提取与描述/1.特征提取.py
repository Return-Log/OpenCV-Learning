import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""harris角点检测"""
# img = cv.imread("jiao.jpg")
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv.cornerHarris(gray,2,3,0.04)
# img[dst>0.01*dst.max()]=[0,0,255]
# plt.imshow(img[:,:,::-1])
# plt.show()

"""shi-tomas"""
img = cv.imread("jiao.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
coners = cv.goodFeaturesToTrack(gray,10,0.3,10)
num = 0
for i in coners:
    x,y = i.ravel()
    cv.circle(img,(x,y),2,(0,255,0),-1)
    num += 1
print(num)
plt.imshow(img[:,:,::-1])
plt.show()