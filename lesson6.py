import cv2

pikachu=cv2.imread("pikachu.png")

print(pikachu.shape)

row,column=pikachu.shape[0:2]

for i in range(row):
    for j in range(column):
        pikachu[i,j]=sum(pikachu[i,j])*0.33


cv2.imshow("pikachu",pikachu)
cv2.waitKey(0)
cv2.destroyAllWindows()