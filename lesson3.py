import cv2
import numpy as np

color1=np.array([18,101,123])
color2=np.array([255,145,64])

img1=np.full((300,300,3),color1,dtype=np.uint8)
img2=np.full((300,300,3),color2,dtype=np.uint8)

add=cv2.add(img1,img2)

addnp=img1+img2

sub=cv2.subtract(img1,img2)

cv2.putText(addnp,"addition result",(30,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2,cv2.LINE_AA)

concatenatedresult=np.concatenate((img1,img2,addnp,sub),axis=1)


cv2.imshow("idk", concatenatedresult)
cv2.waitKey(0)
cv2.destroyAllWindown()