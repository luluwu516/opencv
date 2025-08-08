import cv2
import numpy as np

# Common functions
# Resize the image
path = "Images/luffy.jpg"
img = cv2.imread(path)
print(img.shape)
cropped_img = img[:800, 160:960]
resized_img = cv2.resize(cropped_img, (600, 600))
# resized_img = cv2.resize(cropped_img, (0, 0), fx=2, fy=2)
cv2.imshow("Luffy", img)
cv2.imshow("Luffy (cropped)", cropped_img)
cv2.imshow("Luffy (resized)", resized_img)
# cv2.waitKey(0)

# Convert color
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Luffy (gray)", gray)
# cv2.waitKey(0)

# Gaussian Blur
blur = cv2.GaussianBlur(resized_img, (5, 5), 5)
cv2.imshow("Luffy (blur)", blur)
# cv2.waitKey(0)

# Canny (img, min, max): Find the pixels that are really different from their adjacent pixels (find contour)
# canny = cv2.Canny(resized_img, 150, 200)
canny = cv2.Canny(resized_img, 100, 200)
cv2.imshow("Luffy (contour)", canny)
# cv2.waitKey(0)

# Dilate the image: increase the line width
kernel = np.ones((2, 2), np.uint8)
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]
dilate = cv2.dilate(canny, kernel, iterations=1)
cv2.imshow("Luffy (dilate)", dilate)
# cv2.waitKey(0)

# Erode the image: decrease the line width
erode = cv2.erode(dilate, kernel, iterations=1)
cv2.imshow("Luffy (erode)", erode)
cv2.waitKey(0)
