import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""图像加法"""
a = cv.imread("xx")
b = cv.imread("xx")

img1 = cv.add(a, b)

img2 = a+b

"""图像混合"""
img3 = cv.addWeighted(a, 0.7, b, 0.3, 0)
