# Face Anonymization Scripts

This repository contains six Python scripts for anonymizing faces in images using various techniques. The scripts use OpenCV for face detection and various methods for anonymization. 

## Requirements

* OpenCV
* Python 3.6 or higher
* Numpy (if not already installed with OpenCV)
* PIL (Pillow)

You can install the requirements with pip:

```
pip install opencv-python numpy pillow
```

## Usage

The scripts process all images in the specified `input_folder` and write the anonymized images to the corresponding `output_folder`. 

To run a script:

```
python <script_name>.py
```

Ensure that the input and output folders are correctly specified in each script. 

## Scripts

* `replace_black_bar.py`: Detects faces and places black bars over them.
* `replace_pixel.py`: Detects faces and pixelates them.
* `replace_rect_blur.py`: Detects faces and adds a Gaussian blur over them.
* `replace_swap.py`: Detects faces and swaps the first two faces in each image.
* `replace_emoji.py`: Detects faces and replaces them with a specified emoji.
* `replace_eyes_pixels.py`: Detects faces and replaces the eyes with pixels of the same color as the average color of the face.

## Notes

These scripts are simplified and might not work perfectly in all situations. Some scripts might fail to handle edge cases, such as images with no faces or images where the faces are not in the 'frontal' position. You can adjust the parameters of the face and eye detection to better suit your needs. For more complex tasks, such as accurate face swapping, you might need to use deep learning techniques. 

## License

These scripts are provided under the MIT License. See `LICENSE` for more details.

Remember to update the `<script_name>.py` with the appropriate script you want to run and make sure you have all the necessary dependencies installed on your system.
