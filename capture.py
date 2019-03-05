import cv2
import numpy as np 
import sys

video_path=sys.argv[1]

cap = cv2.VideoCapture(video_path)
ret2=True
i=1
ret=None
frame=None
while True:
    ret, frame = cap.read()
    if ret:
        # frame = cv2.resize(frame, (854,480))
        ret2,frame2 = cv2.imencode('.jpg',frame)
        if ret2:
            sys.stdout.buffer.write(frame2.tobytes())
            
