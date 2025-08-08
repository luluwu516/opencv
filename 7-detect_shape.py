import cv2

shapes = []
path = "Images/A.png"

img = cv2.imread(path)
img = cv2.resize(img, (0, 0), fx=4, fy=4)
img_contour = img.copy()  # the copy of the original image
# print(img.shape)

# Convert the image to grayscale (easier to detect)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find out the contour (Canny)
# (image, lower bound, upper bound)
canny = cv2.Canny(img, 150, 200)

# https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html#gga819779b9857cc2f8601e6526a3a5bc71a48b9c2cb1056f775ae50bb68288b875e
# contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # since A.png has a square inside a square, we can't use only RETR_EXTERNAL
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# print(contours)

for cnt in contours:
    # print(cnt)

    # Draw the contours
    # (canvas, contours, how many(-1 for all), color, width)
    cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 1)

    # Get the area
    area = cv2.contourArea(cnt)
    print(area)
    """
    Output: 
    33489.0  # background
    3118.0
    2116.0
    700.0
    """
    if area > img.shape[0] * img.shape[1] * 0.95:  # ignore the background
        continue

    # Get the perimeter of the contour
    # (contours, close or not)
    peri = cv2.arcLength(cnt, True)
    # print(peri)

    # Get the vertices
    epsilon_factor = 0.02
    epsilon = epsilon_factor * peri  # approximation
    # (contour, approximation, close or not)
    vertices_positions = cv2.approxPolyDP(cnt, epsilon, True)
    vertices = len(vertices_positions)

    # Circle the shapes
    x, y, w, h = cv2.boundingRect(vertices_positions)
    cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 1)

    # Mark the shapes
    if vertices == 3:
        cv2.putText(
            img_contour,
            "Triangle",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            1,
        )
    elif vertices == 4:
        cv2.putText(
            img_contour,
            "Rectangle",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            1,
        )
    elif vertices == 5:
        cv2.putText(
            img_contour,
            "Pentagon",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            1,
        )
    elif vertices >= 6:
        cv2.putText(
            img_contour,
            "Circle",
            (x, y - 5),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            1,
        )

    # Record the shapes
    new_shape = {
        "vertices": vertices,
        "vertices_positions": vertices_positions,
        "perimeter": peri,
        "area": area,
        "is_filled": True,  # TO-DO!!
    }

    shapes.append(new_shape)

# print(shapes)
cv2.imshow("Image", img)
cv2.imshow("Canny", canny)
cv2.imshow("img_contour", img_contour)
cv2.waitKey(0)
