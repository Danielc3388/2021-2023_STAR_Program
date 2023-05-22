"""
python version : 3.7

mediapipe install method
terminal input : pip install mediapipe -i https://pypi.tuna.tsinghua.edu.cn/simple/

"""

import cv2
import mediapipe as mp
import math
import numpy as np
import time
import osascript




mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDrawing = mp.solutions.drawing_utils
STime = 0
vol = 0
maxVol = 500
minVol = 0
camera = cv2.VideoCapture(0)

while (camera.isOpened()):
    suc, img = camera.read()
    conv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    list = []
    result = Hands.process(conv_img)

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            mpDrawing.draw_landmarks(img, hand, mpHands.HAND_CONNECTIONS)
        for i, lm in enumerate(result.multi_hand_landmarks[0].landmark):
            h, w, n = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            list.append([cx, cy])

        if len(list) > 0:
            x1, y1 = list[4][0], list[4][1]
            x2, y2 = list[8][0], list[8][1]

            length = math.hypot(x2-x1,y2-y1)

            maxVol = np.interp(length, [50,300], [500,150])
            minVol = np.interp(length, [50,300], [100,0])

            # vol = "set volume output volume " + str(length)
            # osascript.osascript(vol)

            cv2.rectangle(img, (50,150), (85,500), (255,0,0))
            cv2.rectangle(img, (50, int(maxVol)), (85,500), (255,0,0), cv2.FILLED)


        CTime = time.time()
        fps = 1/(CTime-STime)
        STime = CTime
        cv2.putText(img,str(int(fps)), (50,60), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0),3)

    cv2.imshow("hand tracker", img)
    cv2.waitKey(1)





