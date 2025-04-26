from sklearn.neighbors import KNeighborsClassifier
import csv
import time
from datetime import datetime

import cv2
import pickle
import numpy as np
import os

from win32com.client import Dispatch

cam_video = cv2.VideoCapture(0)

face_var_detection = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

## add sound
def sound_var(str1):
    sound1 = Dispatch(("SAPI.SpVoice"))
    sound1.Speak(str1)

with open('data/user_names.pkl', 'rb') as f:
    LABELS = pickle.load(f)

with open('data/list_face_data.pkl','rb') as f:
    FACES = pickle.load(f)

knn_model  =KNeighborsClassifier(n_neighbors=5)
knn_model.fit(FACES,LABELS)

project_bg_img= cv2.imread('attendence_background.png') 

att_cols = ['Name','Time']


while True:
    ret,frame = cam_video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces_var = face_var_detection.detectMultiScale(gray_img, 1.3 , 5)

    for (x,y,w,h) in faces_var:
        image_cropping = frame[y:y+h, x:x+w, :]
        image_resizing = cv2.resize(image_cropping,(50,50)).flatten().reshape(1,-1)
        output_model =knn_model.predict(image_resizing)
        current_time =time.time()
        date_record = datetime.fromtimestamp(current_time).strftime('%d-%m-%Y')
        time_record = datetime.fromtimestamp(current_time).strftime('%H-%M-%S')
        already_exist_file = os.path.isfile("Attendence\\Attendence_"+date_record+ ".csv")
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,0,255),1)
        cv2.rectangle(frame, (x,y), (x+w, y+h),(50,50,255),2)
        cv2.rectangle(frame, (x,y-40), (x+w, y),(50,50,255),-1)

        cv2.putText(frame, str(output_model[0]), (x,x-15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (10,255,50),1)
        cv2.rectangle(frame, (x,y), (x+w, y+h),(50,50,255),1)

        attendence  = [str(output_model[0]),str(time_record)]
    
    project_bg_img[162:162 +480, 55:55+640] = frame
    
    
    #cv2.imshow("Frame", frame)
    cv2.imshow("Frame", project_bg_img)
    k = cv2.waitKey(1)
    
    if k==ord('o'):
        sound_var("Attendence Recorded..")
        time.sleep(2)
        if already_exist_file:
            with open("Attendence\\Attendence_"+date_record+ ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendence)
                
            csvfile.close()
        else:
            with open("Attendence\\Attendence_"+date_record+ ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(att_cols)
                writer.writerow(attendence)

            csvfile.close()
    
    if k ==ord('q') :
        break

cam_video.release()
cv2.destroyAllWindows()
