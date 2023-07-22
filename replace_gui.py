import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import dlib
import cv2
import os
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog
from anonymize_scripts import *

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('Face Anonymizer')

        self.input_folder = StringVar()
        self.output_folder = StringVar()
        self.person_folder = StringVar()

        Label(self.root, text='Select the method').grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.method = StringVar(self.root)
        self.method.set('Black Bar')  # Default value
        OptionMenu(self.root, self.method, 'Black Bar', 'Pixelate', 'Blur', 'Face Swap', 'Emoji', 'Eye Color').grid(row=0, column=1, padx=10, pady=10, sticky=W)

        Button(self.root, text='Select input folder', command=self.select_input_folder).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        Button(self.root, text='Select output folder', command=self.select_output_folder).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Button(self.root, text='Select person folder', command=self.select_person_folder).grid(row=3, column=0, padx=10, pady=10, sticky=W)

        Button(self.root, text='Run script', command=self.run_script).grid(row=4, column=0, padx=10, pady=10, sticky=W)

    def select_input_folder(self):
        self.input_folder.set(filedialog.askdirectory())

    def select_output_folder(self):
        self.output_folder.set(filedialog.askdirectory())
    
    def select_person_folder(self):
        self.person_folder.set(filedialog.askdirectory())

    def run_script(self):
        method = self.method.get()
        if method == 'Black Bar':
            anonymize_black_bar(self.input_folder.get(), self.output_folder.get(), self.person_folder.get())
        elif method == 'Pixelate':
            anonymize_pixelate(self.input_folder.get(), self.output_folder.get(), self.person_folder.get())
        elif method == 'Blur':
            anonymize_blur(self.input_folder.get(), self.output_folder.get(), self.person_folder.get())
        elif method == 'Face Swap':
            anonymize_face_swap(self.input_folder.get(), self.output_folder.get())
        elif method == 'Emoji':
            anonymize_emoji(self.input_folder.get(), self.output_folder.get(), self.person_folder.get())
        elif method == 'Eye Color':
            anonymize_eye_color(self.input_folder.get(), self.output_folder.get(), self.person_folder.get())


root = Tk()
App(root)
root.mainloop()
