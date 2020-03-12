import cv2 #import opencv 
import time

video=cv2.VideoCapture(0) #open webcam and capture video

a=1
face_cascade=cv2.CascadeClassifier("cascade.xml") #import cascade.xml for face recognition
while True:
    a+=1
    check, frame=video.read()

    faces=face_cascade.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    cv2.imshow("VideCapture", frame)


    key=cv2.waitKey(1)

    if key==ord('q'):
        break
video.release()

cv2.destroyAllWindows()