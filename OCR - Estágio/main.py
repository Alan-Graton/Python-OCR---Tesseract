import cv2
import numpy as np

img = cv2.imread('OpenCV Logo.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('OCR em Python')
cv2.imshow('OCR em Python', img)

cv2.waitKey()