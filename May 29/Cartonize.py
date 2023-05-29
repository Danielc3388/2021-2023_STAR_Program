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

    return img_color

file_name = "Picture.jpg"
result = cartoonizeEffect(file_name)

cv2.imwrite("colorTest.jpg", result)
cv2.imshow("Color Version", result)
cv2.waitKey(0)
cv2.destoryallwindow()

