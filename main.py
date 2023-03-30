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