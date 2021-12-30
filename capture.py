import cv2

first_frame = None

# Create a video object
video = cv2.VideoCapture(0)

# Reads and prints frame
while True:
    check, frame = video.read()

    # Converts color frame to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blurs and updates the gray image
    gray = cv2.GaussianBlur(gray, (31, 31), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    # Show the gray scale images
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    # Press any button to close the window
    key = cv2.waitKey(1)
    print(gray)

    # stops script if 'q' is pressed
    if key == ord('q'):
        break

# Release the camera/video
video.release()
# Destroys all open windows.
cv2.destroyAllWindows()
