import cv2
import os
from PIL import Image

#change the directory to the folder part where the images are located
os.chdir("C:\\Users\\admin\\Desktop\\open cv\\lesson10images")
path="C:\\Users\\admin\\Desktop\\open cv\\lesson10images"

meanh=0
meanw=0

imagesnum=len(os.listdir("."))

for i in os.listdir("."):
    img=Image.open(os.path.join(path,i))
    width,height=img.size
    meanw+=width
    meanh+=height

meanw=meanw//imagesnum
meanh=meanh//imagesnum

print(meanw,meanh)

#resizing the images
for i in os.listdir("."):
    img=Image.open(os.path.join(path,i))
    width,height=img.size
    resizeimg=img.resize((meanw,meanh),Image.LANCZOS)
    resizeimg.save(i)
    print(img.filename.split('\\')[-1], " is resized")


def videocreator():
    videoname="video1.avi"
    os.chdir("C:\\Users\\admin\\Desktop\\open cv\\lesson10images")
    list=[]
    for i in os.listdir("."):
        list.append(i)
    frame=cv2.imread(os.path.join(".",list[0]))
    height,width,layers=frame.shape
    print(frame.shape)
    video=cv2.VideoWriter(videoname,0,1,(width,height))
    for i in list:
        video.write(cv2.imread(os.path.join(".",i)))
    cv2.destroyAllWindows()
    video.release()
videocreator()