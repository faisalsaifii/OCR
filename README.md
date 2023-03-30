# Pytesseract and PIL Image Processing

## Overview

This code demonstrates how to use Pytesseract and PIL (Python Imaging Library) to perform character recognition on an image file. Pytesseract is an OCR (Optical Character Recognition) library that can be used to extract text from images. PIL is a library for opening, manipulating, and saving many different image file formats.

## Installation

Before using this code, make sure you have installed both Pytesseract and PIL. You can do this by running the following commands in your terminal:

```sh
pip install pytesseract
pip install Pillow
```

## Usage

To use this code, follow these steps:

1. Import the necessary libraries: `pytesseract` and `PIL`.
2. Load the image that you want to perform character recognition on using `Image.open()` method. Make sure that the image is in the same directory as your code.
3. Preprocess the image by converting it to grayscale and binarizing it.
4. Perform character recognition using `pytesseract.image_to_string()` method.
5. Post-process the recognized text as per your requirement.

## Code Explanation

```python
import pytesseract
from PIL import Image

# Load image
img = Image.open('image.jpg')

# Preprocessing
img = img.convert('L') # convert to grayscale
img = img.point(lambda x: 0 if x<128 else 255, '1') # binarize image

# Character Recognition
text = pytesseract.image_to_string(img)

# Post-processing
print(text)
```

1. We first import the necessary libraries - pytesseract and PIL.
2. We then load the image image.jpg using Image.open() method and store it in the img variable.
3. We preprocess the image by converting it to grayscale and binarizing it using the convert() and point() methods, respectively. The point() method is used to set the threshold for binarization. Pixels with values less than 128 are set to 0 (black) and those with values greater than or equal to 128 are set to 255 (white).
4. We then perform character recognition on the preprocessed image using pytesseract.image_to_string() method and store the recognized text in the text variable.
5. Finally, we post-process the recognized text as per our requirement. In this case, we print the recognized text using the print() function.

## Conclusion

This code demonstrates how to use Pytesseract and PIL to perform character recognition on an image file. You can modify the preprocessing and post-processing steps as per your requirement.
