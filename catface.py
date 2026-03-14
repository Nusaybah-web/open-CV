import cv2

harfile="haarcascade_frontalcatface.xml"
detector=cv2.CascadeClassifier(cv2.data.haarcascades+harfile)

webcam=cv2.VideoCapture(0)

while True:
    value, img=webcam.read()
    if not value:
        continue
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    catface=detector.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in catface:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        cat=grayimg[y:y+h,x:x+y]

    cv2.imshow("img",img)
    k=cv2.waitKey(10)
    if k==27:
        break

webcam.release()
cv2.destroyAllWindows()