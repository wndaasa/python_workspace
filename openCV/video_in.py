import sys
import cv2

cap = cv2.VideoCapture('.\\openCV\\video1.mp4')

if not cap.isOpened():
    print('Camera open failed!')
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    inversed = ~frame
    
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)
    
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()