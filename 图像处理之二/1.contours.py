import cv2
import cv2 as cv
import numpy as np

img = cv2.imread("contours.png")
print(img.shape)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape)

# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
print(binary.shape)

# 轮廓查找
_, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

# cv2.imshow("binary", binary)
# cv2.waitKey(0)