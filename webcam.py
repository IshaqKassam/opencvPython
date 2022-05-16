import cv2

cap = cv2.VideoCapture(2) #id 0 for inbuilt webcam, id2 for the usb camera
cap.set(3, 640) #width
cap.set(4, 480) #height
cap.set(10, 100)#brightness

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break