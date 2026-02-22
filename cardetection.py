import cv2,os

xml="cars.xml"
width,height=130,100


cardector=cv2.CascadeClassifier(xml)
cars=cv2.VideoCapture("Cars.mp4")


while True:
    returnvalue,img=cars.read()
    if returnvalue==False:
            continue
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    car=cardector.detectMultiScale(grayimg,1.1,2)
    for (x,y,w,h) in car:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)

    cv2.imshow("img",img)
    k=cv2.waitKey(10)
    if k==27:
        break
cv2.destroyAllWindows()