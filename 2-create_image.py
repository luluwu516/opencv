import cv2
import numpy as np
import random

# Create a 300 * 300 RGB image
img = np.empty((300, 300, 3), np.uint8)  # 8 bit -> 256 (0-255)
for row in range(300):
    for col in range(300):
        img[row][col] = [255, 0, 0]  # blue square

cv2.imshow("img", img)

# Create a noise image
noise = np.empty((300, 300, 3), np.uint8)  # 8 bit -> 256 (0-255)
for row in range(300):
    for col in range(300):
        noise[row][col] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]
cv2.imshow("noise", noise)
cv2.waitKey(0)
