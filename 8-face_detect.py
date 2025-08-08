import cv2

path = "Images/lulu.jpg"
img = cv2.imread(path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the model (downloaded from https://github.com/opencv/opencv)
faceCascade = cv2.CascadeClassifier("face_detect.xml")

# (image, scale down number, amount of adjacent square)
faceRect = faceCascade.detectMultiScale(gray, 1.1, 10)
# print(len(faceRect))

# Circle the face
for x, y, w, h in faceRect:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

cv2.imshow("img", img)
cv2.waitKey(0)
