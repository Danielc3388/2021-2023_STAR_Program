import cv2

def cartoonizeEffect(img_rgb):
    img_rgb = cv2.imread(img_rgb)

    img_color = img_rgb
    for i in range (2):
        img_color = cv2.pyrDown(img_color)

    for i in range(50):
        img_color = cv2.bilateralFilter(img_color,9,9,7)

    for i in range(2):
        img_color = cv2.pyrUp(img_color)

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 3)

    img_edge = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)

    (x,y,z) = img_color.shape
    img_edge = cv2.resize(img_edge, (y,x))
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

    return cv2.bitwise_and(img_color, img_edge)

file_name = "Picture.jpg"
result = cartoonizeEffect(file_name)

cv2.imwrite("colorTest.jpg", result)
cv2.imshow("Color Version", result)
cv2.waitKey(0)
cv2.destoryallwindow()

