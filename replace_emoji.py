import cv2
import os
from PIL import Image

input_folder = './input/'
output_folder = './emoji_output/'
emoji_path = './emoji.png'  # replace with path to your emoji image

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

for filename in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, filename))
    emoji = cv2.imread(emoji_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        emoji_resized = cv2.resize(emoji, (w, h))
        img[y:y+h, x:x+w] = emoji_resized

    cv2.imwrite(os.path.join(output_folder, filename), img)
