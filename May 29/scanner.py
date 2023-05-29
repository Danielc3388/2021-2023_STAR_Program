import cv2
import imutils
import numpy as np

def order_points(pts):      #top_left, clockwised
    rect = np.zeros((4,2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_points_transform(img,pts):
    rect = order_points(pts)
    (tl,tr,br,bl) = rect
    #((x1-x2)^2+(y1-y2)^2)^-1
    widthA = np.sqrt(((tl[0]-tr[0])**2) + ((tl[1]-tr[1])**2))
    widthB = np.sqrt(((bl[0]-br[0])**2) + ((bl[1]-br[1])**2))
    heightA = np.sqrt(((tl[0]-bl[0])**2) + ((tl[1]-bl[1])**2))
    heightB = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([0,0], [maxWidth-1, 0], [maxWidth-1, maxHeight-1], [0, maxHeight-1], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(img, M, (maxWidth,maxHeight))
    return warped

def main():
    image = cv2.imread("Picture.jpg")
    ratio = image.shape[0]/500.0
    ori = image.copy()
    image = imutils.resize(image, height=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5), 0)
    edge = cv2.Canny(gray, 75, 200)

    cnts = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[0:5]
    for c in cnts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c, 0.02*peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break

    else:
        print('No Document found')
        return

    cv2.drawContours(image, [screenCnt], -1, (0,255,0), 2)
    warped = four_points_transform(ori, screenCnt.reshape(4,2)*ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    T = cv2.threshhold(warped, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSH)[1]

    cv2.imshow("Original", imutils.resize(ori, heigh=1000))
    cv2.imshow("Scanned", imutils.resize(warped, heigh=1000))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

