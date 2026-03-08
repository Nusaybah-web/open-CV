import cv2,os

harfile="haarcascade_frontalface_default.xml"
harfilesmile="haarcascade_smile.xml"


facedecetor=cv2.CascadeClassifier(cv2.data.haarcascades+harfile)
smiledetector=cv2.CascadeClassifier(cv2.data.haarcascades+harfilesmile)


webcam=cv2.VideoCapture(0)


while True:
    value, img=webcam.read()
    if not value:
        continue
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    faces=facedecetor.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        face=grayimg[y:y+h,x:x+y]
        smile=smiledetector.detectMultiScale(face,scaleFactor=1.8,minNeighbors=20,minSize=(25,25))
        for (sx,sy,sw,sh) in smile:
            cv2.rectangle(img,(x+sx-4,sy+y),(x+sx-4+sw,sy+y+h),(0,0,255),2)
      

    cv2.imshow("img",img)
    k=cv2.waitKey(10)
    if k==27:
        break
        
webcam.relese()
cv2.destroyAllWindows()
