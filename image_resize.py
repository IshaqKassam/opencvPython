import cv2
import numpy as np

img = cv2.imread('Resources/lena.jpeg')
print(img.shape)

imgResize = cv2.resize(img, (300, 200))#width then height

imgCropped = img[0:100, 0:100]

cv2.imshow("image", img)
cv2.imshow("Resize", imgResize)
cv2.imshow("cropped", imgCropped)

cv2.waitKey(0)