
from boltiot import Sms, Bolt
import json, time
import cv2
import numpy as np

API_KEY = 'YourAPI'
DEVICE_ID = 'YourBoltID' 
   

mybolt = Bolt(API_KEY, DEVICE_ID)

def alert2():
    response = mybolt.analogWrite('0', '100')
    print(str(response))

def detect(frame, thresh = 1100):
    
    fgmask= foog.apply(frame)

    ret,fgmask = cv2.threshold(fgmask , 250 , 255, cv2.THRESH_BINARY)

    fgmask = cv2.erode(fgmask, kernel ,iterations = 1)
    fgmask = cv2.dilate(fgmask , kernel , iterations = 4)

    contours,hierarchy = cv2.findContours(fgmask , cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        cnt = max(contours, key = cv2.contourArea)
        area = cv2.contourArea(cnt)
        if area > thresh:
            return True
    else:
        return False




capture = cv2.VideoCapture("enteryourip/video")

start = 0

kernel = None

global foog
    
foog = cv2.createBackgroundSubtractorMOG2(detectShadows = True ,varThreshold = 50 , history = 2800)

thresh = 3000

while(1):
    ret,frame = capture.read()
    if not ret:
        break
    
    status = detect(frame,thresh)
    if status:
        if start == 0:
            alert2()
        if time.time()- start > 100:
            alert2()
            start = time.time()
    if not status and time.time()- start > 100:
        start =0 
        

    cv2.imshow('Combined',cv2.resize(frame,None,fx= 0.65, fy = 0.65))
            
    k = cv2.waitKey(40) & 0xff
    if k == ord('w'):
        break
        
capture.release()
cv2.destroyAllWindows()
