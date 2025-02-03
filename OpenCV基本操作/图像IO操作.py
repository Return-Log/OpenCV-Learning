import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread("1.png", 0)  # 读取图像

# # opencv中显示图像
# cv.imshow("image", img)
# cv.waitKey(0)


# matplotlib中显示图像
# 需将opencv的BGR通道转换为RGB通道
if len(img.shape) == 2:
    # 灰度图像，直接显示
    plt.imshow(img, cmap='gray')
elif len(img.shape) == 3:
    # 彩色图像，反转颜色通道顺序后显示
    plt.imshow(img[:,:,::-1])
plt.show()


# # 保存图像
# cv.imwrite("save.png", img)