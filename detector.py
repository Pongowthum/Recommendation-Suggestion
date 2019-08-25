import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
rec=cv2.createLBPHFaceRecognizer();
rec.load('recognizer/trainningData.yml')
id=0

def getFromDB(Id):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM Criminal WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    record=None
    for row in cursor:
        record=row
    conn.close()
    return record
cam=cv2.VideoCapture(0);
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,2,1,0,4)

while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        profile=getFromDB(id)
        if(conf<50):
            if(profile!=None):
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[0]),(x,y+h),font,255)
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),(x,y+h+30),font,255)
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[2]),(x,y+h+60),font,255)
                cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[3]),(x,y+h+90),font,255)
        else:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face",img);
    if(cv2.waitKey(1)==ord('q')):
       break
cam.release()
cv2.destroyAllWindows()
