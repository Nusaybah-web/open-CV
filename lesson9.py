import cv2
import numpy as np

blob=cv2.imread("blob.jpg")

sblob=cv2.SimpleBlobDetector_Params()
#area filtering
sblob.filterByArea=True
sblob.minArea=100
#circularaty filtering
sblob.filterByCircularity=True
sblob.minCircularity=0.9
#convexity
sblob.filterByConvexity=True
sblob.minConvexity=0.2
#inertia filling 
sblob.filterByInertia=True
sblob.minInertiaRatio=0.01

blobdictetor=cv2.SimpleBlobDetector_create(sblob)

dictor=blobdictetor.detect(blob)
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(blob,dictor,blank,(255,255,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
text=cv2.putText(blobs,"the number of circles is: "+str(len(dictor)),(10,505),cv2.FONT_HERSHEY_COMPLEX,1,(200,20,150),2,cv2.LINE_AA)

cv2.imshow("blobs",blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()