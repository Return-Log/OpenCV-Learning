import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

"""视频读取与显示"""
cap = cv.VideoCapture("video.mp4")
# while(cap.isOpened()):
#     ret,frame = cap.read()
#     if ret == True:
#         cv.imshow("frame",frame)
#     if cv.waitKey(25)&0xFF == ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()

"""图像保存"""
width = int(cap.get(3))
height = int(cap.get(4))
out = cv.VideoWriter("out.avi",cv.VideoWriter_fourcc("M","J","P","G"),16,(width,height))
while(True):
    ret,frame = cap.read()
    if ret == True:
        out.write(frame)
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()

