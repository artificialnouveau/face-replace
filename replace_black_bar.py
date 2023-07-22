import cv2
import os
import numpy as np
import glob

input_folder = './input/'
output_folder = './blur_output/'
person_folder = './person/'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Train the recognizer with images of the specific person
person_images = [cv2.imread(img, cv2.IMREAD_GRAYSCALE) for img in glob.glob(person_folder + "*.jpg")]
person_faces = [face_cascade.detectMultiScale(img, 1.1, 4)[0] for img in person_images]
person_labels = [0 for _ in person_images]  # Here we use 0 as the label for the specific person

recognizer.train(person_faces, np.array(person_labels))

def anonymize_blur(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face)
            if label == 0:  # If the face is recognized as the specific person
                face = cv2.GaussianBlur(face, (99, 99), 30)
                img[y:y+h, x:x+w] = face

        cv2.imwrite(os.path.join(output_folder, filename), img)
