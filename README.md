# Face Recognition Attendance System 🎯
This project uses OpenCV, Face Recognition, and Machine Learning (KNN Classifier) to automatically detect faces and record attendance in real time with a webcam. It also saves attendance logs in .csv files and provides real-time audio feedback on successful entry!

## 🚀 Features
* Detect faces using Haar Cascade Classifier (haarcascade_frontalface_default.xml)
* Capture and store face data in real-time
*Train a K-Nearest Neighbors (KNN) model on captured faces
* Mark attendance with timestamp
* Auto-create daily attendance CSV files
* Real-time audio confirmation ("Attendance Recorded") using Windows Text-to-Speech
* Beautiful UI using OpenCV overlays
* Streamlit support (optional) for web-based view

## 🛠️ Tech Stack
* Python 3.9+
* OpenCV
* face_recognition
* scikit-learn (KNN)
* pickle
* Streamlit (optional for web UI)
* pyttsx3 / win32com for audio (Windows)

