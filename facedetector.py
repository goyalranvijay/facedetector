import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
cap=cv2.VideoCapture(0)
while True:
    
    ret,img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
    scaleFactor=1.1,
    minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
    cv2.imshow("Faces", img)
    if cv2.waitKey(100)& 0xFF==ord('t'):
        break
cap.release()
cv2.destroyAllWindows()