import cv2 #import opencv 

face_cascade=cv2.CascadeClassifier("cascade.xml") #import cascade.xml for face recognition

img=cv2.imread("<image_name>") #import an image(use locally downloaded image)

gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting color image into grayscale

faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

# resized=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("Gray", img)

cv2.waitKey(0)

cv2.destroyAllWindows()