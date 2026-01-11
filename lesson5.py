import cv2

pikachu=cv2.imread("pikachu.png")
ocv=cv2.imread("opencvpicture.png")
gwh=cv2.imread("girlwithahat.png")
gg=cv2.imread("gray.png")

#Gaussian Blur
gblur=cv2.GaussianBlur(ocv,(7,7),5)

#median blur
mblur=cv2.medianBlur(gwh,9)

#bilatral filter
bf=cv2.bilateralFilter(gg,15,200,200)

#borders
border=cv2.copyMakeBorder(pikachu,100,100,100,100,cv2.BORDER_CONSTANT,value=(0,0,255))

cv2.imshow("blur",border)
cv2.waitKey(0)
cv2.destroyAllWindows()