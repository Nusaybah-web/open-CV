import cv2
import numpy as np

#img=cv2.imread("pikachu.png",cv2.IMREAD_COLOR)
#img=cv2.imread("pikachu.png",cv2.IMREAD_GRAYSCALE)
img=cv2.imread("pikachu.png")
b,g,r=cv2.split(img)

"""cv2.imshow("pikachu image", img)
cv2.waitKey(0)

cv2.imshow("blue saturation pikachu image", b)
cv2.waitKey(0)

cv2.imshow("green saturation pikachu image", g)
cv2.waitKey(0)

cv2.imshow("red saturaion pikachu image", r)
cv2.waitKey(0)"""

#creating blank channel for merging

zeros=np.zeros_like(b)

blueimg=cv2.merge([b,zeros,zeros])
cv2.imshow("blue image",blueimg)

greenimg=cv2.merge([zeros,g,zeros])
cv2.imshow("green image",greenimg)

redimg=cv2.merge([zeros,zeros,r])
cv2.imshow("red image",redimg)

cv2.waitKey(0)
cv2.destroyAllWindows()