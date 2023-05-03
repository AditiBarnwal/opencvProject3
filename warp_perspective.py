import cv2
import numpy as np

img = cv2.imread('bag.jpg')
reSize = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)

width, height = 250, 350

pts1 = np.float32([[44, 305], [147, 422], [212, 197], [318, 308]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(reSize, matrix, (width, height))
# print(pts1)
# for x in range(0, 4):
#     cv2.circle(reSize, (pts1[x][0], pts[x][1]), 5, (0, 66, 245), cv2.FILLED)
cv2.circle(reSize, (44, 305), 5, (0, 66, 245), cv2.FILLED)
cv2.imshow("resize", reSize)
cv2.imshow("imgOutput", imgOutput)
cv2.waitKey(0)
