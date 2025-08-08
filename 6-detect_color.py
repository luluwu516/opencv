import cv2
import numpy as np


def empty(v):
    pass


path = "Images/luffy.jpg"
img = cv2.imread(path)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# Create a track bar for hue, saturation, and value (brightness)
cv2.namedWindow("TrackBar")
# (window_name, width, height)
# cv2.resizeWindow("TrackBar", 640, 320)

# Ceate control bars
# (label, on which window, initial, max, function)
cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)  # hue: 0-179
cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)  # saturation: 0-255
cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)  # value: 0-255
cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)

# Convert BRG color to HSV color (easier to filter the color)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    # Get the values from the track bars
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Filter the color
    # (which image, lower bound, upper bound)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Luffy (original)", img)
    cv2.imshow("Luffy (HSV)", hsv)
    cv2.imshow("Luffy (mask)", mask)
    cv2.imshow("Result", result)
    cv2.waitKey(1)
