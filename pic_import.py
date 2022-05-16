import cv2

print("Package imported")

img = cv2.imread('Resources/lena.jpeg')

cv2.imshow("output", img)
cv2.waitKey(0)