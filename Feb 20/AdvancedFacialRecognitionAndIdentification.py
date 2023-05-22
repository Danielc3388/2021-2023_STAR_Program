import cv2
import numpy as np
import face_recognition
import os

"""
faceLocB = face_recognition.face_locations(imgB)[0]
encodeB = face_recognition.face_encodings(imgB)[0]
cv2.rectangle(imgB, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 3)

faceLocC = face_recognition.face_locations(imgC)[0]
encodeC = face_recognition.face_encodings(imgC)[0]
cv2.rectangle(imgC, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 3)

result = face_recognition.compare_faces([encodeB], encodeA)
dist = face_recognition.face_distance([encodeB], encodeA)
"""

def findEncoding(img):
    encodeList = []
    for i in img:
        cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(i)[0]
        encodeList.append(encode)

    return encodeList

path = "Advanced"
images = []     #storing all jpeg inside path
names = []      #storing all name inside path
myList = os.listdir(path)
for img in myList:
    curImg = cv2.imread(f'{path}/{img}')
    if os.path.splitext(img)[0] != ".DS_Store":
        images.append(curImg)
        names.append(os.path.splitext(img)[0])

print(images)


print(names)

encodeListDone = findEncoding(images)
print(len(encodeListDone))

cap = cv2.VideoCapture(2)

while True:
    suc, img = cap.read()
    imgSmall = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgSmall)
    encodeCurFrame = face_recognition.face_encodings(imgSmall,facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListDone, encodeFace)
        faceDist = face_recognition.face_distance(encodeListDone,encodeFace)
        print(faceDist)
        print(matches)
        matchIndex = np.argmin(faceDist)

        if matches[matchIndex]:
            name = names[matchIndex]
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1,y1), (x2, y2), (0,255,0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))

    cv2.imshow("Face Identification", img)
    cv2.waitKey(1)


