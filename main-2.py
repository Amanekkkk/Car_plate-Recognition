import cv2
import pytesseract
from PIL import Image

img = cv2.imread('lprecog/detections/detection1.png')

string = pytesseract.image_to_string(img)

for i in string:
    if i.isalpha() or i.isnumeric():
        print(i, end='')