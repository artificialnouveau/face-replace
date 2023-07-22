import cv2
import os
import numpy as np

input_folder = './input/'
output_folder = './eye_color_output/'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        avg_color = [int(face[:, :, i].mean()) for i in range(face.shape[-1])]
        eyes = eyes_cascade.detectMultiScale(face)
        for (ex, ey, ew, eh) in eyes:
            face[ey:ey+eh, ex:ex+ew] = avg_color

    cv2.imwrite(os.path.join(output_folder, filename), img)
