import cv2
import numpy as np

path = "Images/A.png"

# Show the image
img = cv2.imread(path)
cv2.imshow("img", img)
# cv2.waitKey(2000)  # wait 2s if no key is detected, close the window

# Resize the image
img = cv2.imread(path)
resized_img1 = cv2.resize(img, (300, 300))  # resize the img to 300x300
resized_img2 = cv2.resize(img, (0, 0), fx=2, fy=2)  # scale the img by a factor of two
cv2.imshow("img", img)
cv2.imshow("resized_img1", resized_img1)
cv2.imshow("resized_img2", resized_img2)
# cv2.waitKey(0)  # wait for a key to be enter, and then close the window

# Image's array
# row, col, RGB(but the order is BGR)
print(img.shape)  # Output: (184, 184, 3)
print(img[0][0])  # Output: [255 255 255]
# Blue Red Green (BRG)
# [255 0 0] -> Blue

# Crop the image
# img = cv2.imread(path)
cropped_img = img[:100, :100]
# cv2.imshow("img", img)
cv2.imshow("cropped_img", cropped_img)
cv2.waitKey(0)
