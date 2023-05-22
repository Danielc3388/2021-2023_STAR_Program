import cv2 as cv

camera = cv.VideoCapture(2)

while True:
    success, img = camera.read()
    cv.imshow("Windows",img)
    cv.waitKey(1)
