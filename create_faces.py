import cv2
import pickle
import numpy as np
import os

cam_video = cv2.VideoCapture(0)

face_var_detection = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')




list_face_data = []

i=0

user_name_input = input ("Your good name, please?")

while True:
    ret,frame = cam_video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    faces_var = face_var_detection.detectMultiScale(gray_img, 1.3 , 5)

    for (x,y,w,h) in faces_var:
        image_cropping = frame[y:y+h, x:x+w, :]
        image_resizing = cv2.resize(image_cropping,(50,50))
        if len(list_face_data) <=100 and i%10==0:
            list_face_data.append(image_resizing)
        i=i+1
        cv2.putText(frame, "Count of Image Captured: " + str(len(list_face_data )), (30,30),cv2.FONT_HERSHEY_DUPLEX,1,(10,180,255),2)
        cv2.rectangle(frame, (x,y), (x+w, y+h),(50,50,255),2)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k ==ord('q') or len(list_face_data)==100:
        break

cam_video.release()
cv2.destroyAllWindows()

list_face_data  = np.asarray(list_face_data)
list_face_data = list_face_data.reshape(100,-1)

if 'user_names.pkl' not in os.listdir('data/'):
    user_names = [user_name_input]*100
    with open('data/user_names.pkl', 'wb') as f:
        pickle.dump(user_names,f)
else:
    with open('data/user_names.pkl', 'rb') as f:
        user_names = pickle.load(f)

    user_names = user_names+[user_name_input]*100
    with open('data/user_names.pkl', 'wb') as f:
        pickle.dump(user_names,f)


if 'list_face_data.pkl' not in os.listdir('data/'):
    with open('data/list_face_data.pkl', 'wb') as f:
        pickle.dump(list_face_data,f)
else:
    with open('data/list_face_data.pkl', 'rb') as f:
        faces_var = pickle.load(f)
    print(len(faces_var), len(list_face_data))
    
    faces_var = np.append(faces_var,list_face_data, axis=0)
    with open('data/list_face_data.pkl', 'wb') as f:
        pickle.dump(user_names,f)