import cv2
import mediapipe as mp

mp_pose=mp.solutions.pose
mp_drawing=mp.solutions.drawing_utils

pose=mp_pose.Pose(min_detection_confidence=0.5,min_tracking_confidence=0.5)

webcam=cv2.VideoCapture(0)

while webcam.isOpened():
    bool,img=webcam.read()
    if not bool:
        print("faild to grab frame")
        break
    color=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(color)
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(img,results.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()