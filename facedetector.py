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
    i=1
    for (x, y, w, h) in faces:
        cv2.putText(img,org=(x-10,y-10),fontScale=0.5,fontFace=cv2.FONT_ITALIC,color=(255,255,0),thickness=1,lineType=cv2.LINE_AA,text=f"FACE {i}")
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)
        i+=1
    cv2.imshow("Faces", img)
    if cv2.waitKey(100)& 0xFF==ord('t'):
        break
cap.release()
cv2.destroyAllWindows()