import cv2
import numpy as np

office=cv2.imread("office.jpg")
ohsv=cv2.cvtColor(office,cv2.COLOR_BGR2HSV)

#defining the 1 red range
lr1=np.array([0,40,40])
ur1=np.array([0,255,255])
mask1=cv2.inRange(ohsv,lr1,ur1)

#defining thw 2 red range
lr2=np.array([160,40,40])
ur2=np.array([180,255,255])
mask2=cv2.inRange(ohsv,lr2,ur2)

#combining both masks
mask=mask1+mask2

ed=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
de=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)

variable=cv2.bitwise_not(mask)

cv2.imshow("mask1",mask1)
cv2.waitKey(0)
cv2.imshow("mask2",mask2)
cv2.waitKey(0)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.imshow("ed",ed)
cv2.waitKey(0)
cv2.imshow("de",de)
cv2.waitKey(0)
cv2.imshow("variable",variable)
cv2.waitKey(0)