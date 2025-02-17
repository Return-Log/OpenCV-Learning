import cv2.cv2
import matplotlib.pyplot as plt
from cv2 import cv2

img = cv2.imread("face.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face_cas = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_cas = cv2.CascadeClassifier("haarcascade_eye.xml")

face_cas.load("haarcascade_frontalface_default.xml")
eyes_cas.load("haarcascade_eye.xml")

face_rects = face_cas.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))
for facerect in face_rects:
    x,y,w,h = facerect
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    roi_color = img[y:y+h,x:x+w]
    roi_gray = gray[y:y+h,x:x+w]
    eyes = eyes_cas.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)

plt.imshow(img[:,:,::-1])
plt.show()