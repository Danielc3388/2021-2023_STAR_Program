import cv2

cap = cv2.VideoCapture(0)

for i in range(5):
    suc, img = cap.read()
suc, img = cap.read()

tracker_types = ["MIL", "BOOSTING", "KCF", "TLD", "MEDIANFLOW", "CSRT"]

print("Available Tracker" + str(tracker_types))
type = input("Choose the type of tracker: ")
if type not in tracker_types:
    print("Using default tracker: MEDIANFLOW")
    type = "MEDIANFLOW"

if type == "MIL":                                   #Good at tracking object that look the same and don't change shape or disappear
    tracker = cv2.TrackerMIL_create()
elif type == "BOOSTING":                            #Good at tracking object that look the same and don't change shape or disappear
    tracker = cv2.legacy.TrackerBoosting_create()
elif type == "KCF":
    tracker = cv2.TrackerKCF_create()               #Good at traacking object that looks the same, but faster and more accurate
elif type == "TLD":
    tracker = cv2.legacy.TrackerTLD_create()        #Gppd at tracking object that change shape or disappear, but less accurate
elif type == "MEDIANFLOW":
    tracker = cv2.legacy.TrackerMedianFlow_create() #average performance, simple and fast
elif type == "CSRT":
    tracker = cv2.legacy.TrackerCSRT_create()       #very accurate abd works for all kind of object under any condition, but it is slower


bbox = cv2.selectROI("Tracker", img, False)
tracker.init(img, bbox)

cv2.destroyAllWindows()
while True:

    suc, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        (x,y,w,h) = bbox
        cv2.putText(img, "Tracking" + type, (40,50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)
        cv2.rectangle(img,(int(x), int(y)), (int(x)+int(w), int(y) + int(h)), (255,0,0), 2)
    else:
        cv2.putText(img, "Lost", (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    cv2.imshow("Object Tracker", img)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()