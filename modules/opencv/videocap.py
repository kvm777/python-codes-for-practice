import cv2

cap = cv2.VideoCapture(0)

cap.set(3,320)
cap.set(4,240)

while True:
    success , img = cap.read()
    cv2.imshow("image", img)
    cv2.waitKey(1)