# Python Face Anonymization Scripts

This project includes six Python scripts for various face anonymization techniques. These scripts can anonymize faces in images using blurring, black bars, pixelation, face swapping, emoji replacement, and eye replacement.

Each script can operate in two modes:

1. General anonymization: In this mode, all faces in each image will be anonymized.
2. Person-specific anonymization: In this mode, only the faces of a specific individual will be anonymized. The individual is specified by providing one or more images of the person. If the specified individual is not found in the image, no anonymization is applied.

## Prerequisites
- Python 3.8 or later
- OpenCV (cv2)
- numpy
- tkinter

## Scripts

### 1. anonymize_blur.py
This script applies a Gaussian blur to anonymize faces in the images.

### 2. anonymize_black_bar.py
This script places a black bar over detected faces in the images.

### 3. anonymize_pixelate.py
This script pixelates the faces detected in the images for anonymization.

### 4. anonymize_swap.py
This script swaps faces detected in the images. This script only works when there are at least two faces in the image.

### 5. anonymize_emoji.py
This script replaces the faces detected in the images with a default emoji.

### 6. anonymize_eye_color.py
This script replaces the eyes with pixels of the same color as the average color of the face.

Each script takes two mandatory arguments - input_folder and output_folder - and an optional third argument - person_folder. The input_folder is the directory from where the script will read the images, the output_folder is where it will write the anonymized images. The person_folder is the optional directory containing images of the specific person to be anonymized.

## How to Run the Scripts
```shell
python <script_name> input_folder output_folder [person_folder]
```
Replace `<script_name>` with the name of the script you wish to run, `input_folder` with the directory containing your input images, `output_folder` with the directory where you want the output images to be saved, and `person_folder` (if provided) with the directory containing one or more images of the specific person to be anonymized.

For example:
```shell
python anonymize_blur.py ./input/ ./output/ ./person/
```

## GUI Application
In addition to the scripts, a GUI application is provided for a more user-friendly experience. The application allows the user to select an anonymization method from a dropdown menu, specify the input and output folders, and optionally specify a folder containing images of a specific person to anonymize. The application can be run with the following command:

```shell
python app.py
```

## Limitations
These scripts are intended to serve as simple examples of face anonymization. They may not work well in all situations or for all images, especially in cases of non-frontal or partially occluded faces, faces with different expressions or accessories, or low-quality images.
