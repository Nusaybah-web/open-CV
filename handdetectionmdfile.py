import cv2
import mediapipe as mp

#inisialising mediapipe handdetection
mphands=mp.solutions.hands
hands=mphands.Hands(min_detection_confidence=0.8,min_tracking_confidence=0.8)
drawing=mp.solutions.drawing_utils

webcam=cv2.VideoCapture(0)

#fingercounting
def counting(landmarks):
    thumbtip=landmarks.landmark[4]
    indextip=landmarks.landmark[8]
    middletip=landmarks.landmark[12]
    ringtip=landmarks.landmark[16]
    pinkeytip=landmarks.landmark[20]

    open=0

    if thumbtip.x>landmarks.landmark[3].x:
        open+=1
    if indextip.y<landmarks.landmark[7].y:
        open+=1
    if middletip.y<landmarks.landmark[11].y:
        open+=1
    if ringtip.y<landmarks.landmark[14].y:
        open+=1
    if pinkeytip.y<landmarks.landmark[19].y:
        open+=1
    
    return open

while True:
    bool,img=webcam.read()
    if not bool:
        break
    color=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #process the frame
    result=hands.process(color)
    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            drawing.draw_landmarks(img,i,mphands.HAND_CONNECTIONS)
            #count the number if fingers that are open
            count=counting(i)
            cv2.putText(img,"the number of fingers open= "+str(count),(20,20),cv2.FONT_HERSHEY_COMPLEX,1,(200,20,150),2)
    cv2.imshow("hands",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()