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

def anonymize_swap(input_folder, output_folder, person_folder=None):
    if person_folder and os.listdir(person_folder):
        person_images = [cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2GRAY) for img in glob.glob(person_folder + "*.jpg")]
        person_faces = [face_cascade.detectMultiScale(img, 1.1, 4)[0] for img in person_images]
        person_labels = [0 for _ in person_images]

        recognizer.train([cv2.resize(img[y:y+h, x:x+w], (200, 200)) for img, (x, y, w, h) in zip(person_images, person_faces)], np.array(person_labels))

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) >= 2:
            for i in range(0, len(faces), 2):
                (x1, y1, w1, h1), (x2, y2, w2, h2) = faces[i], faces[i+1]
                face1 = np.copy(img[y1:y1+h1, x1:x1+w1])
                face2 = np.copy(img[y2:y2+h2, x2:x2+w2])
                
                face1_gray = cv2.cvtColor(face1, cv2.COLOR_BGR2GRAY)
                face2_gray = cv2.cvtColor(face2, cv2.COLOR_BGR2GRAY)

                if person_folder and os.listdir(person_folder):
                    label1, _ = recognizer.predict(cv2.resize(face1_gray, (200, 200)))
                    label2, _ = recognizer.predict(cv2.resize(face2_gray, (200, 200)))

                    if label1 == 0:
                        img[y1:y1+h1, x1:x1+w1] = cv2.resize(face2, (w1, h1))
                    if label2 == 0:
                        img[y2:y2+h2, x2:x2+w2] = cv2.resize(face1, (w2, h2))

        cv2.imwrite(os.path.join(output_folder, filename), img)
