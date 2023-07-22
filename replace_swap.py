import cv2
import os
import numpy as np

input_folder = './input/'
output_folder = './swap_output/'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) >= 2:
        (x1, y1, w1, h1), (x2, y2, w2, h2) = faces[0], faces[1]
        face1 = np.copy(img[y1:y1+h1, x1:x1+w1])
        face2 = cv2.resize(np.copy(img[y2:y2+h2, x2:x2+w2]), (w1, h1))
        img[y1:y1+h1, x1:x1+w1] = face2
        img[y2:y2+h2, x2:x2+w2] = cv2.resize(face1, (w2, h2))

    cv2.imwrite(os.path.join(output_folder, filename), img)
