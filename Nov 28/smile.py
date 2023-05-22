import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarCascade_frontalface_default.xml")
eye = cv2.CascadeClassifier(cv2.data.haarcascades + "haarCascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarCascade_smile.xml")

def detect(grayImg, frame):
    faces = face_cascade.detectMultiScale(grayImg, 1.2, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 2) #BGR
        s_gray = grayImg[y:y+h, x:x+w]
        s_colour = frame[y:y+h, x:x+w]


        smiles = smile_cascade.detectMultiScale(s_gray, 1.8 ,15) #second parameter 1.7-2.0 third parameter 15+
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(s_colour, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 2)  # BGR
            print("smile detected")

    return frame

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    screen = detect(grayImg, frame)

    cv2.imshow("Smile detection", screen)

    if cv2.waitKey(1) and 0xff == ord('q'):
        cap.release()
        cv2.destroyAllWindows
        break


