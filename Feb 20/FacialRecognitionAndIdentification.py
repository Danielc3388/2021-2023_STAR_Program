import cv2
import numpy as np
import face_recognition

imgA = face_recognition.load_image_file("Basic/A.jpeg")
imgA = cv2.cvtColor(imgA, cv2.COLOR_BGR2RGB)
imgB = face_recognition.load_image_file("Basic/B.jpeg")
imgB = cv2.cvtColor(imgB, cv2.COLOR_BGR2RGB)
imgC = face_recognition.load_image_file("Basic/B(2).jpeg")
imgC = cv2.cvtColor(imgC, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgA)[0]
encodeA = face_recognition.face_encodings(imgA)[0]
cv2.rectangle(imgA, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 3)

faceLocB = face_recognition.face_locations(imgB)[0]
encodeB = face_recognition.face_encodings(imgB)[0]
cv2.rectangle(imgB, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 3)

faceLocC = face_recognition.face_locations(imgC)[0]
encodeC = face_recognition.face_encodings(imgC)[0]
cv2.rectangle(imgC, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,0), 3)

result = face_recognition.compare_faces([encodeB], encodeA)
dist = face_recognition.face_distance([encodeB], encodeA)

print(result,  dist)

cv2.imshow("A", imgA)
cv2.imshow("B", imgB)
cv2.imshow("C", imgC)

cv2.waitKey(0)