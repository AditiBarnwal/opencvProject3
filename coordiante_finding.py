# import cv2
# import numpy as np
#
#
# # def click_events(event, x, y, flags, params):
# #     if event == cv2.EVENT_LBUTTONDOWN:
# #         print('left click')
# #         print(f'({x},{y})')
# #
# #         cv2.putText(resize, f'({x},{y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (245, 66, 203), 2)
# #         cv2.circle(resize, (x, y), 3, (167, 66, 245), -1)
# #203, 66, 245
#
# img = cv2.imread('bag.jpg')
# reSize = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
# pts1 = np.float32([[44, 305], [147, 422], [212, 197], [318, 308]])
# print(pts1)
#
# # cv2.namedWindow('Point Coordinates')
# # cv2.setMouseCallback('Point Coordinates', click_events)
#
# # for i in range(0, 4):
# #     cv2.circle(reSize, (pts1[i][0], pts1[i][1]), 5, (0, 66, 245), cv2.FILLED)
# cv2.circle(reSize, (44, 305), 5, (0, 66, 245), cv2.FILLED)
# # while True:
# #    # cv2.imshow('Point Coordinates', resize)
# #
# #
# #    if cv2.waitKey(1) & 0xff == ord('q'):
# #        break
#
# cv2.imshow('resize', reSize)
# cv2.waitKey(0)
