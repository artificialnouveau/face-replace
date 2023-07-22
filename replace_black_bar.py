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

def anonymize_blur(input_folder, output_folder, person_folder=None):
    if person_folder and os.listdir(person_folder):
        # Train the recognizer with images of the specific person
        person_images = [cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY) for img in glob.glob(person_folder + "*.jpg")]
        person_faces = [face_cascade.detectMultiScale(img, 1.1, 4)[0] for img in person_images]
        person_labels = [0 for _ in person_images]  # Here we use 0 as the label for the specific person

        recognizer.train([cv2.resize(img[y:y+h, x:x+w], (200, 200)) for img, (x, y, w, h) in zip(person_images, person_faces)], np.array(person_labels))

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            if person_folder and os.listdir(person_folder):
                label, confidence = recognizer.predict(face)
                if label == 0:  # If the face is recognized as the specific person
                    face = cv2.GaussianBlur(img[y:y+h, x:x+w], (99, 99), 30)
                    img[y:y+h, x:x+w] = face
            else:  # If no person_folder is provided or person_folder is empty, blur all faces
                face = cv2.GaussianBlur(img[y:y+h, x:x+w], (99, 99), 30)
                img[y:y+h, x:x+w] = face

        cv2.imwrite(os.path.join(output_folder, filename), img)

# Call the function
anonymize_blur(input_folder, output_folder, person_folder)
