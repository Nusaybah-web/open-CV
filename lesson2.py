import cv2

img=cv2.imread("umbrella.webp")
img2=cv2.imread("umbrella.webp",0)

b,g,r=cv2.split(img)

print(img2.shape)

cv2.imshow("umbrella image", img)
cv2.waitKey(0)

cv2.imshow("blue saturation umbrella image", b)
cv2.waitKey(0)

cv2.imshow("green saturation umbrella image", g)
cv2.waitKey(0)

cv2.imshow("red saturaion umbrella image", r)
cv2.waitKey(0)

cv2.destroyAllWindown()