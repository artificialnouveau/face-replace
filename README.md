# Face Anonymization Scripts

This repository contains Python scripts for six different methods of face anonymization:

1. **Black Bar:** This script detects faces in images and overlays a black rectangle over each detected face.

2. **Pixelate:** This script detects faces in images and pixelates the region of each detected face.

3. **Blur:** This script detects faces in images and applies a blur effect over each detected face.

4. **Face Swap:** This script detects faces in images and swaps the faces. If there is only one face, it throws an error. It can handle multiple faces in the image.

5. **Emoji:** This script detects faces in images and replaces each face with an emoji.

6. **Eye Color:** This script detects faces in images and changes the eye color to the average color of the face.

Each script reads images from a specified input directory, applies the face anonymization method, and writes the anonymized images to a specified output directory.

## Dependencies

These scripts depend on several Python libraries, including OpenCV, Pillow, NumPy, and Tkinter. Some scripts also require the Dlib library and a pre-trained facial landmark predictor model file.

You can install the dependencies with pip:

```
pip install opencv-python-headless pillow numpy tkinter dlib
```

You can download the pre-trained model file from [here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2). Remember to decompress the downloaded file to get the `.dat` file, and place it in the same directory as your script.


## Scripts

* `replace_black_bar.py`: Detects faces and places black bars over them.
* `replace_pixel.py`: Detects faces and pixelates them.
* `replace_rect_blur.py`: Detects faces and adds a Gaussian blur over them.
* `replace_swap.py`: Detects faces and swaps all the faces in each image.
* `replace_emoji.py`: Detects faces and replaces them with a specified emoji.
* `replace_eyes_pixels.py`: Detects faces and replaces the eyes with pixels of the same color as the average color of the face.

  
## Usage

There is a GUI application that lets you select which face anonymization method to use, and which directories to use for input and output. You can run the application with the command:

```
python app.py
```

In the GUI, you can select the face anonymization method from the drop-down menu, select the input and output directories by clicking the "Select input folder" and "Select output folder" buttons, respectively, and start the face anonymization process by clicking the "Run script" button.


## Limitations and Future Work

These scripts are intended to serve as simple examples of face anonymization. They may not work well in all situations or for all images, especially in cases of non-frontal or partially occluded faces, faces with different expressions or accessories, or low-quality images.

Future work could include improving the face detection and anonymization techniques, supporting different image formats and color spaces, and adding more face anonymization methods.

