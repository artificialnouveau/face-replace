import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import dlib
import cv2
import os
from tkinter import messagebox

def anonymize_black_bar(input_folder, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            img[y:y+h, x:x+w] = [0, 0, 0]  # black color

        cv2.imwrite(os.path.join(output_folder, filename), img)

    messagebox.showinfo('Information', 'Black Bar anonymization completed successfully.')


# Pixelate Anonymization
def anonymize_pixelate(input_folder, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = img[y:y+h, x:x+w]
            face = cv2.resize(face, (16, 16))
            face = cv2.resize(face, (w, h), interpolation=cv2.INTER_NEAREST)
            img[y:y+h, x:x+w] = face

        cv2.imwrite(os.path.join(output_folder, filename), img)

    messagebox.showinfo('Information', 'Pixelation anonymization completed successfully.')


# Blur Anonymization
def anonymize_blur(input_folder, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            face = img[y:y+h, x:x+w]
            blurred_face = cv2.GaussianBlur(face, (99, 99), 30)
            img[y:y+h, x:x+w] = blurred_face

        cv2.imwrite(os.path.join(output_folder, filename), img)

    messagebox.showinfo('Information', 'Blur anonymization completed successfully.')

# Face Swap Anonymization
def anonymize_face_swap(input_folder, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        if len(faces) < 2:
            messagebox.showwarning('Warning', f"Image {filename} contains less than 2 faces, face swap cannot be performed")
        else:
            face_images = []
            for (x, y, w, h) in faces:
                face = np.copy(img[y:y+h, x:x+w])
                face_images.append((face, x, y, w, h))

            for i in range(len(face_images)):
                face, x, y, w, h = face_images[i]
                next_face, _, _, next_w, next_h = face_images[(i+1)%len(face_images)]
                resized_face = cv2.resize(next_face, (w, h))
                img[y:y+h, x:x+w] = resized_face

            cv2.imwrite(os.path.join(output_folder, filename), img)

    messagebox.showinfo('Information', 'Face swap anonymization completed successfully.')

def anonymize_emoji(input_folder, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the emoji image
    emoji = cv2.imread('emoji.png')

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            # Resize the emoji to the size of the detected face
            resized_emoji = cv2.resize(emoji, (w, h))
            # Replace the face with the emoji
            img[y:y+h, x:x+w] = resized_emoji

        cv2.imwrite(os.path.join(output_folder, filename), img)

    messagebox.showinfo('Information', 'Emoji anonymization completed successfully.')


def anonymize_eye_color(input_folder, output_folder):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load the facial landmark predictor from dlib
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    for filename in os.listdir(input_folder):
        img = cv2.imread(os.path.join(input_folder, filename))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            # Convert the (x, y, w, h) tuple to a dlib rectangle
            dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
            
            # Get the facial landmarks
            shape = predictor(gray, dlib_rect)
            
            # Get the average color of the face
            avg_color = cv2.mean(img[y:y+h, x:x+w])[:3]
            
            # Define a mask for the eyes (assume landmarks 36-41 are for the left eye, and 42-47 are for the right eye)
            mask = np.zeros((h, w), dtype=np.uint8)
            for i in range(36, 48):
                cv2.circle(mask, (shape.part(i).x - x, shape.part(i).y - y), 2, (255), thickness=-1)
            
            # Blur the mask to get a smoother transition
            mask = cv2.GaussianBlur(mask, (7, 7), 0)
            
            # Create a color image of the same size as the mask, filled with the average color
            color_img = np.full((h, w, 3), avg_color, dtype=np.uint8)
            
            # Use the mask to mix the color image with the original image
            img[y:y+h, x:x+w] = cv2.bitwise_and(color_img, color_img, mask=mask) + cv2.bitwise_and(img[y:y+h, x:x+w], img[y:y+h, x:x+w], mask=cv2.bitwise_not(mask))

        cv2.imwrite(os.path.join(output_folder, filename), img)

    messagebox.showinfo('Information', 'Eye color anonymization completed successfully.')


class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Face Anonymizer')

        self.input_folder = None
        self.output_folder = None

        self.methods = ['Black Bar', 'Pixelate', 'Blur', 'Face Swap', 'Emoji', 'Eye Color']

        self.var = StringVar(self.root)
        self.var.set(self.methods[0])

        Label(self.root, text='Select method:').grid(row=0, column=0, padx=10, pady=10, sticky=W)
        OptionMenu(self.root, self.var, *self.methods).grid(row=0, column=1, padx=10, pady=10, sticky=W+E)

        Button(self.root, text='Select input folder', command=self.select_input_folder).grid(row=1, column=0, padx=10, pady=10, sticky=W+E)
        Button(self.root, text='Select output folder', command=self.select_output_folder).grid(row=1, column=1, padx=10, pady=10, sticky=W+E)

        Button(self.root, text='Run script', command=self.run_script).grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=W+E)

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory()

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory()

    def run_script(self):
        method = self.var.get()
        if not self.input_folder or not self.output_folder:
            messagebox.showwarning('Warning', 'Please select both input and output folders')
        else:
            if method == 'Black Bar':
                anonymize_black_bar(self.input_folder, self.output_folder)
            elif method == 'Pixelate':
                anonymize_pixelate(self.input_folder, self.output_folder)
            elif method == 'Blur':
                anonymize_blur(self.input_folder, self.output_folder)
            elif method == 'Face Swap':
                anonymize_face_swap(self.input_folder, self.output_folder)
            elif method == 'Emoji':
                anonymize_emoji(self.input_folder, self.output_folder)
            elif method == 'Eye Color':
                anonymize_eye_color(self.input_folder, self.output_folder)
            else:
                messagebox.showwarning('Warning', f'Method {method} not implemented')

root = Tk()
app = App(root)
root.mainloop()

