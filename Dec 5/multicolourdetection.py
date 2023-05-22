import cv2
import numpy as np
from numpy import ndarray

camera = cv2.VideoCapture(0)

while True:

    _, img = camera.read()
    hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    Lower_red = np.array([140,85,110], np.uint8)
    Upper_red = np.array([180,255,110], np.uint8)
    red_mask = cv2.inRange(hsvFrame, Lower_red, Upper_red)

    Lower_green = np.array([25, 50, 70], np.uint8)
    Upper_green = np.array([100, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, Lower_green, Upper_green)

    Lower_blue = np.array([90,80,10], np.uint8)
    Upper_blue = np.array([120,255,255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, Lower_blue, Upper_blue)

    kernel = np.ones ((5,5), "uint8",)

    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(img, img, mask = red_mask)

    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(img, img, mask=green_mask)

    blue_mask = cv2.dilate(blue_mask, kernel)
    res_blue = cv2.bitwise_and(img, img, mask=blue_mask)

    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for frame, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area >= 300:
            x,y,w,h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
            cv2.putText(img, "Red",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255))

#green

    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for frame, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area >= 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(img, "Green",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

#blue

    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for frame, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if area >= 300:
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
            cv2.putText(img, "Blue",(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

    cv2.imshow("MultiColorDetector", img)
    if cv2.waitKey(4) and 0xFF == ord ('q'):
        camera.release()
        cv2.destroyAllWindows()
        break