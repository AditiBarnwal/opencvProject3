import cv2
import numpy as np

circles = np.zeros((4, 2), np.int8)
counter = 0


def mousePoints(event, x, y, params, flags):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(x, y)


while True:
    img = cv2.imread("glow.jpg")
    if counter == 4:
        width, height = 250, 350
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("OutputImg", imgOutput)

    for x in range(0, 4):
        cv2.circle(img, (int(circles[x][0]), int(circles[x][1])), 5, (0, 0, 255), -1)

    cv2.imshow("original img", img)
    cv2.setMouseCallback("original img", mousePoints)
    # cv2.imshow("OutputImg", imgOutput)
    cv2.waitKey(0)
