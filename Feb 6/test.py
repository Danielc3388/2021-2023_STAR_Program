import cv2
import mediapipe as mp

mpHand = mp.solutions.hands
Hands = mpHand.Hands()
handDrawing = mp.solutions.drawing_utils
thumb = (4,2)
fingers = [(8,6),(12,10),(16,14),(20,18)]

camera = cv2.VideoCapture(0)

while camera.isOpened():
    count = 0
    handNo = 0
    list = []
    suc, img = camera.read()
    conv_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = Hands.process(conv_image)

    if result.multi_hand_landmarks:
        for i in result.multi_hand_landmarks:
            handDrawing.draw_landmarks(img, i, mpHand.HAND_CONNECTIONS)


    cv2.imshow("Hand Recognition", img)
    cv2.waitKey(1)