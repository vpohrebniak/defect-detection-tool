# Defect Detection Tool

A simple tool for detecting defects in a new image by comparing it to a reference image.  
The application uses OpenCV to compare pixel differences and calculate a similarity score.

## Table of Contents
1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [License](#license)

## Features
- **Image selection via GUI**: Easily browse and select two images using a dialog box.
- **MD5 hash verification**: Ensures you are not comparing the same or identical images.
- **Defect detection**: Provides a similarity percentage to quickly determine whether the new image has significant differences.
- **Intuitive interface**: Built with `tkinter` for a simple, user-friendly experience.

## Requirements
- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/) (for image processing)
- [NumPy](https://pypi.org/project/numpy/) (for array operations)
- Tkinter (usually included in standard Python installations)
- hashlib (part of the standard Python library)

## Installation
1. **Clone this repository** or download the ZIP:
   ```bash
   git clone https://github.com/vpohrebniak/defect-detection-tool.git
2. **Navigate to the project folder**:
   ```bash
   cd defect-detection-tool
3. **Install the required packages:**
   ```bash
   pip install opencv-python numpy
Note: tkinter and hashlib are included in the standard library on most operating systems.

## Usage
1. **Ensure** you have all dependencies installed.
2. **Run** the tool:
```bash
python defect_detection.py
```
3. A window will appear with the following:
  - **Select** Images button: Click to choose the reference image and then the new image.
  - The tool will compare the images and display either a success message if the detail has no defects or a warning if it detects significant differences.

## How It Works

1. **Image Selection**
The user is prompted to select two images: a reference image and a new detail image.
2. **MD5 Hash Check**
The script calculates the MD5 hash of both images to ensure they are not identical.
3. **Image Comparison**
- Both images are resized to 300×300 pixels to have consistent dimensions.
- The script computes the absolute difference between the images using cv2.absdiff.
- The difference is converted to grayscale, thresholded, and then the number of differing pixels is calculated.
- The similarity percentage is derived from the ratio of identical pixels to total pixels.
4. **Result**
- If the similarity is above 80%, the tool concludes that the detail has no defects.
- Otherwise, it shows a warning that the new image has defects or significant differences.

