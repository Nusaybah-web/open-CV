import cv2, os
import numpy as np

harfile="haarcascade_frontalface_default.xml"

namefolder="facialrecognitions"

print("recognising face, please ensure sufficient lighting")

imges,lables,names,id=([],[],{},0)

if not os.path.exists(namefolder) or not os.listdir(namefolder):#checking if the folder exists or if its empty
    print("the directory is empty or does not exist")
    exit()

for person in os.listdir(namefolder):
    personpath=os.path.join(namefolder,person)#building the full path of the person in the datasafe
    #checking itf actually a folder
    if os.path.isdir(personpath):
        names[id]=person#adding key-value parn to dictonary
        for imagefile in os.listdir(personpath):#loop through images inside personsfolder
            path=os.path.join(personpath,imagefile)
            img=cv2.imread(path,0)
            imges.append(img)
            lables.append(id)
        id+=1

width,height=130,100
imges,lables=[np.array(i) for i in [imges,lables]]
#training the recogniser
recogniser=cv2.face.LBPHFaceRecognizer_create()
#learning the facialpatterns
recogniser.train(imges,lables)
#loadingfacedetectionmodle
facecascade=cv2.CascadeClassifier(harfile)
webcam=cv2.VideoCapture(0)

while True:
    succes,frame=webcam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(gray,1.3,5)
    #process each face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        face=gray[y:y+h,x:x+w]
        resize=cv2.resize(face,(width,height))
        #facerecognitionprediction
        prediction=recogniser.predict(resize)
        if prediction[1]<100:
            cv2.putText(frame,f"{names[prediction[0]]}-{prediction[1]:.0f}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,150),2)
        else:
            cv2.putText(frame,"unknown",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,150),2)
    
    cv2.imshow("faces",frame)
    k=cv2.waitKey(10)
    if k==27:
        break
webcam.release()
cv2.destroyAllWindows()