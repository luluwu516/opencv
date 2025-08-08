import cv2

# Read from the video file
path = "Videos/mouse.mp4"
video_cap = cv2.VideoCapture(path)

while True:
    # ret: boolean, return true if it gets next frame
    # frame: picture
    video_ret, video_frame = video_cap.read()

    if video_ret:
        video_frame = cv2.resize(video_frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("Video", video_frame)
    else:
        break

    if cv2.waitKey(1) == ord("q"):  # waitKey controls the speed of the video
        break


# Read from the webcam
cam_cap = cv2.VideoCapture(0)  # 0: default webcam

while True:
    cam_ret, cam_frame = cam_cap.read()

    if cam_ret:
        cv2.imshow("Webcam", cam_frame)
    else:
        break

    if cv2.waitKey(1) == ord("q"):
        break
