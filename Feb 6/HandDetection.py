"""
Warning:
    follow the following specification for installation if you are using mac m1/m2 or newer chips, or you
    will get error when installing mediapipe

python version : 3.7

mediapipe install method
terminal input : pip install mediapipe -i https://pypi.tuna.tsinghua.edu.cn/simple/

"""


import cv2
import mediapipe as mp

mpHand = mp.solutions.hands
Hands = mpHand.Hands()
handDrawing = mp.solutions.drawing_utils
thumb = (4,2)
fingers = [(8,6),(12,10),(16,14),(20,18)]

camera = cv2.VideoCapture(0)

while True:
    count = 0
    handNo = 0
    list = []
    suc, img = camera.read()
    conv_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    result = Hands.process(conv_image)

    if result.multi_hand_landmarks:
        for id, l in enumerate(result.multi_hand_landmarks[handNo].landmark):
            t,d,p = img.shape
            cx,cy = int(l.x*d), int(l.y*t)
            list.append((cx,cy))
        for i in result.multi_hand_landmarks:
            handDrawing.draw_landmarks(img, i, mpHand.HAND_CONNECTIONS)

        for coor in fingers:
            if list[coor[0]][1]<list[coor[1]][1]:
                count += 1

        if list[thumb[0]][0] > list[thumb[1]][0]:
            count += 1

        cv2.putText(img,str(count),(100,100),cv2.FONT_HERSHEY_PLAIN,12,(255,0,0),12)


    cv2.imshow("Hand Recognition", img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

