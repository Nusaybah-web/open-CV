import cv2
import numpy as np

img=cv2.imread("house.jpg")
img2=cv2.imread("mountain.jpg")
pika=cv2.imread("pikachu.png")

sum=cv2.addWeighted(img,0.5,img2,0.1,0)
sub=cv2.subtract(img,img2)

#img resizing
resize=cv2.resize(img,(800,600))

#erosion
kernel=np.ones((10,10),np.uint8)
erosion=cv2.erode(pika,kernel)

#cv2.imshow("images",sum)
#cv2.imshow("images",sub)
#cv2.imshow("images",resize)
cv2.imshow("images",erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()