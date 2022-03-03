from pickle import TRUE
from time import ctime
import cv2
import mediapipe
import time

cap = cv2.VideoCapture('PoseVideos/1.mp4')
pTime=0,
while TRUE:
    success, img = cap.read()
         
    
    cTime = time.time()
    fps= 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,
     (2550,0,0),3)
    
    img= cv2.resize(img,(960,540))
    cv2.imshow("Image",img)
    cv2.waitKey(1)