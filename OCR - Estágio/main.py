import re
import cv2
import pytesseract as tess
from pytesseract import Output
from matplotlib import pyplot as plt

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

IMG_DIR = 'images/'
PDF_DIR = 'PDFs/'

image = cv2.imread(IMG_DIR + 'digits-task.jpg')
b,g,r = cv2.split(image)
rgb_img = cv2.merge([r,g,b])

# Imprimindo o todo o Conteúdo Imagem
custom_config = r'-l eng --oem 3 --psm 6'
print(tess.image_to_string(image, config = custom_config))

# Imprimindo somente os Dígitos da Imagem
custom_config = r'--oem 3 --psm 6 outputbase digits'
print(tess.image_to_string(image, config = custom_config))

plt.imshow(rgb_img)
plt.title('Sample Table')
plt.show()