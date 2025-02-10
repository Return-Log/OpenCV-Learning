import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""模板匹配"""
# img = cv.imread("gao.jpeg")
# template = cv.imread("bird.jpeg")
# res = cv.matchTemplate(img,template,cv.TM_SQDIFF_NORMED)
# minval, maxval, minloc, maxloc = cv.minMaxLoc(res)
# top_left = minloc
# h,w = template.shape[:2]
# bottom_right = (top_left[0]+w,top_left[1]+h)
# cv.rectangle(img,top_left,bottom_right,(255,0,0),4)
# plt.imshow(img[:,:,::-1])
# plt.show()

"""霍夫线检测"""
# img = cv.imread("gao.jpeg")
# edges = cv.Canny(img,50,150)
# lines = cv.HoughLines(edges,0.8,np.pi/180,300)
# for line in lines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = rho*a
#     y0 = rho*b
#     x1 = int(x0+1000*(-b))
#     y1 = int(y0+1000*a)
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * a)
#     cv.line(img,(x1,y1),(x2,y2),(0,255,0))
# plt.imshow(img[:,:,::-1])
# plt.show()

"""霍夫圆检测"""
star = cv.imread("circle.jpg")
gray = cv.cvtColor(star,cv.COLOR_BGR2GRAY)
img = cv.medianBlur(gray,7)
circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,200,param1=100,param2=50,minRadius=0,maxRadius=0)
circles = circles[0, :].astype(int)
for i in circles:
    cv.circle(star,(i[0],i[1]),i[2],(0,255,0),2)
    cv.circle(star,(i[0], i[1]), 2, (255, 0, 0), -1)
plt.imshow(star[:,:,::-1])
plt.show()

