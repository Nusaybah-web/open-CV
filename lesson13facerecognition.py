import cv2
import os

harfile="haarcascade_frontalface_default.xml"

namefolder="facialrecognitions"
subfolder="nusaybah"
path=os.path.join(namefolder,subfolder)
if not os.path.isdir(path):
    os.mkdir(path)

width,height=130,100
facedecetor=cv2.CascadeClassifier(harfile)

webcam=cv2.VideoCapture(0)

count=1
while count<30:
    value,img=webcam.read()
    if not value:
        continue
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facedecetor.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        face=grayimg[y:y+h,x:x+w]
        faceresize=cv2.resize(face,(width,height))
        cv2.imwrite("%s/%s.png"%(path, count), faceresize)
    count+=1

    cv2.imshow("img",img)
    k=cv2.waitKey(10)
    if k==27:
        break