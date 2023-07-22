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

    if len(faces) < 2:
        raise ValueError(f"Image {filename} contains less than 2 faces, face swap cannot be performed")
    else:
        face_images = []
        for (x, y, w, h) in faces:
            face = np.copy(img[y:y+h, x:x+w])
            face_images.append((face, x, y, w, h))

        # Swap faces
        for i in range(len(face_images)):
            face, x, y, w, h = face_images[i]
            next_face, _, _, next_w, next_h = face_images[(i+1)%len(face_images)]  # Get the next face in the list
            resized_face = cv2.resize(next_face, (w, h))
            img[y:y+h, x:x+w] = resized_face

    cv2.imwrite(os.path.join(output_folder, filename), img)
