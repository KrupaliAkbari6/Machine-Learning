import cv2

#Step-1 : Read The Image
img=cv2.imread("baby.jpg",cv2.IMREAD_COLOR)

#Step-2 : Load The Classifier
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Step-3 : Convert Image Into Greyscale
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Step-4 : Use Classifier To Detect Object In Grayscale Image
faces=face_cascade.detectMultiScale(grey_img,1.1,4)
print(faces)

#Step-5 : Plot Detected Object Using Classifier On The Actual Image
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)

#Step-6 : Show The Image
cv2.imshow("Face Detector",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
