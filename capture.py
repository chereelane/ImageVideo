import cv2, time

# Create a video object
video = cv2.VideoCapture(0)

check, frame = video.read()

print(check)
print(frame)

# Set time to hold for 3 seconds
time.sleep(6)
cv2.imshow("Capturing", frame)


# Press any button to close the window

cv2.waitKey(0)
# Release the camera/video
video.release()
# Destroys all open windows.
cv2.destroyAllWindows()
