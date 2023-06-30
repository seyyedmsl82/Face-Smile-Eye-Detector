import cv2
import os


face_cascade = cv2.CascadeClassifier('frontalface.xml')
eye_cascade = cv2.CascadeClassifier('eye.xml')
smile_cascade = cv2.CascadeClassifier('Smile.xml')


def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 15)
  
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 2)

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.8, 5)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), ((ex + ew), (ey + eh)), (0, 0, 255), 2)

    return frame

video_capture = cv2.VideoCapture(0)
while video_capture.isOpened():
    _, frame = video_capture.read() 
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    canvas = detect(gray, frame)   
    
    cv2.imshow('Video', canvas) 
                      
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
        break

video_capture.release()
cv2.destroyAllWindows()
