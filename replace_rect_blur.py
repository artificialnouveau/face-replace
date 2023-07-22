import cv2
import os

input_folder = './input/'
output_folder = './blur_output/'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        face = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(face, (99, 99), 30)
        img[y:y+h, x:x+w] = blur

    cv2.imwrite(os.path.join(output_folder, filename), img)
