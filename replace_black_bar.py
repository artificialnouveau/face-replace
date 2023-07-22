import cv2
import os
from PIL import Image

input_folder = './input/'
output_folder = './black_bar_output/'
person_folder = './person/'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def anonymize_black_bar(input_folder, output_folder, person_folder):
    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        person_files = glob.glob(person_folder + "*.jpg")

        if len(person_files) > 0:
            for (x, y, w, h) in faces:
                face = gray[y:y+h, x:x+w]
                label, confidence = recognizer.predict(face)
                if label == 0:
                    img[y:y+h, x:x+w] = 0
        else:
            for (x, y, w, h) in faces:
                img[y:y+h, x:x+w] = 0

        cv2.imwrite(os.path.join(output_folder, filename), img)


anonymize_black_bar(input_folder, output_folder, person_folder)
