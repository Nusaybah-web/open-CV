import cv2

pikachu=cv2.imread("pikachu.png")
house=cv2.imread("house.jpg")

print(pikachu.shape)

row,column=pikachu.shape[0:2]

for i in range(row):
    for j in range(column):
        pikachu[i,j]=sum(pikachu[i,j])*0.33


cv2.imshow("pikachu",pikachu)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotating an image

#getRotationMatric2D cerats a matric needed for transformation

matrix=cv2.getRotationMatrix2D((column/2,row/2),45,1)
rotate=cv2.warpAffine(pikachu,matrix,(column,row))

cv2.imshow("rotate",rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()

#edgedetection

edges=cv2.Canny(house,1,200)

cv2.imshow("edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()