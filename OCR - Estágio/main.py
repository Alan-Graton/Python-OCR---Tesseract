import re
import cv2
import pytesseract as tess
import numpy as np
from pytesseract import Output
from matplotlib import pyplot as plt
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

IMG_DIR = 'images/'
PDF_DIR = 'PDFs/'

im = Image.open('Mels.png')

texto = tess.image_to_string(im, lang = 'eng')
print(texto)

texto = re.sub('\n', '\t\n', texto)
print(texto)