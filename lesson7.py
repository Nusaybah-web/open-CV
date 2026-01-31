import cv2

#drawing a line

house=cv2.imread("house.jpg")

line=cv2.line(house,(200,500),(600,800),(200,20,150),5)

rect=cv2.rectangle(house,(120,50),(620,300),(200,20,150),-1)

cir=cv2.circle(house,(970,50),50,(200,20,150),-1)

house=cv2.putText(house,"house",(1070,780),cv2.FONT_HERSHEY_COMPLEX,1,(200,20,150),2,cv2.LINE_AA)

cv2.imshow("line",line)
cv2.waitKey(0)
cv2.destroyAllWindows()