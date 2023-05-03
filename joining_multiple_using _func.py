import cv2
import numpy as np
import myutils

framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)
cap.set(3, framewidth)
cap.set(4, frameheight)

while True:
    success, img = cap.read()
    cv2.imshow("result", img)
    kernel = np.ones((5, 5), np.uint8)
    print(kernel)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 200)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

    imgBlack = np.zeros((200, 200), np.uint8)

    StackImages = myutils.stackImages(0.5, ([img, imgGray, imgBlur, img, imgGray, imgBlur],
                                    [imgCanny, imgEroded, imgDilation, img, imgBlack, imgGray],
                                    [imgCanny, imgEroded, imgDilation, img, imgBlur, imgGray]))
    cv2.imshow("stackedImages", StackImages)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
