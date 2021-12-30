import cv2, time

# Create a video object
video = cv2.VideoCapture(0)

a = 1

# Reads and prints frame
while True:
    a = a + 1
    check, frame = video.read()

    print(check)
    print(frame)

    # Converts color frame to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Show the gray scale images
    cv2.imshow("Capturing", gray)

    # Press any button to close the window
    key = cv2.waitKey(1)

    # stops script if 'q' is pressed
    if key == ord('q'):
        break
print(a)
# Release the camera/video
video.release()
# Destroys all open windows.
cv2.destroyAllWindows()
