import cv2
import numpy as np

img1 = cv2.imread("glow.jpg")
img2 = cv2.imread("glow.jpg")

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (0, 0), None, 0.2, 0.2)
img2 = cv2.resize(img2, (0, 0), None, 0.2, 0.2)

ver = np.vstack((img1, img2))
hor = np.hstack((img1, img2))

cv2.imshow("ver", ver)
cv2.imshow("hor", hor)
cv2.waitKey(0)
