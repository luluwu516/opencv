import cv2
import numpy as np

img = np.zeros((600, 600, 3), np.uint8)
# print(img)
"""
[[[0 0 0]
  [0 0 0]
    ...
  [0 0 0]
  [0 0 0]]

[[[0 0 0]
  [0 0 0]
    ...
  [0 0 0]
  [0 0 0]]

...

[[[0 0 0]
  [0 0 0]
    ...
  [0 0 0]
  [0 0 0]]
"""
# Equal to:
# img = np.empty((600, 600, 3), np.uint8)
# for row in range(600):
#     for col in range(600):
#         img[row][col] = [0, 0, 0]  # black


# Line and Rectangle
# (canvas, begin, end, color, width)
cv2.line(img, (0, 0), (400, 300), (0, 255, 255), 1)  # yellow \ line
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)  # green \ line

cv2.rectangle(img, (0, 0), (300, 400), (0, 0, 255), 2)  # red rectangle outline
cv2.rectangle(img, (300, 400), (600, 600), (0, 0, 255), cv2.FILLED)  # red rectangle

# Circle
# (canvas, center, radius, color, width)
cv2.circle(img, (img.shape[1] // 2, img.shape[0] // 2), 30, (0, 255, 255), 2)

# Text
# (canvas, text, leftdowncorner, font, size, color, width)
cv2.putText(img, "Hello", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 4)

cv2.imshow("Image", img)
cv2.waitKey(0)
