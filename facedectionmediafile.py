import cv2
import mediapipe as mp #googles aidetection ai framework
print(dir(mp))

facedetect=mp.solutions.face_detection#facedetector tool
drawing=mp.solutions.drawing_uteis#drawing on the face
#turn om facedetection
face=facedetect.FaceDetection(min_detection_confdience=0.2)
webcam=cv2.VideoCapture(0)

while webcam.isOpened():
    bool,img=webcam.read()
    if not bool:
        print("failed to grab frame")
        break
    rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #ditect faces
    result=face.process(rgb) #rturns a list if deticted faces
    if result.detections:
        for i in result.detections:
            drawing.draw_detection(img,i)
    cv2.imshow("facedetecton",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
