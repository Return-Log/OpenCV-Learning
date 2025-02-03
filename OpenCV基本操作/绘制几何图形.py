import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def make_black_background():
    """创建黑色背景图"""
    img = np.zeros((512, 512, 3), np.uint8)
    return img

def draw(text):
    """绘制图形"""
    img = make_black_background()
    cv.line(img, (0, 0), (500, 500), (255, 0, 0), 5)
    cv.circle(img, (256, 256), 100, (0, 0, 255), -1)
    cv.rectangle(img, (50, 50), (480, 480), (0, 255, 0), 5)
    cv.putText(img, text, (50, 50), cv.FONT_HERSHEY_COMPLEX ,2, (0, 255, 0), 3)
    return img


if __name__ == '__main__':
    img = draw("hello world!")
    plt.imshow(img[:, :, ::-1])
    plt.show()
