import cv2
import pathlib

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print (cascade_path)

classify = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0)

while True :
    _, img = camera.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = classify.detectMultiScale(grayImg, scaleFactor = 1.3, minNeighbors = 3, minSize = (50,50), flags = cv2.CASCADE_SCALE_IMAGE)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)

    cv2.imshow("Face Recognition", img)
    cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllwincows
