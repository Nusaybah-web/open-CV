import cv2
import numpy as np

pikachu=cv2.imread("pikachu.png")

gray=cv2.cvtColor(pikachu,cv2.COLOR_BGR2GRAY)
blur=cv2.blur(gray,(3,3))

circle=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=30,maxRadius=40)

if circle is not None:
    circle=np.uint16(np.around(circle))
    print(circle)
    for i in circle[0,:]:
        x,y,r=i[0],i[1],i[2]
        cv2.circle(pikachu,(x,y),r,(200,20,150),3)
        cv2.imshow("line",pikachu)
        cv2.waitKey(0)
    

cv2.destroyAllWindows()