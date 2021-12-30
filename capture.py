import cv2, time, pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

# Create a video object
video = cv2.VideoCapture(0)

# Reads and prints frame
while True:
    check, frame = video.read()
    # indicates if there is motion in the frame; if there is no motion - status = 0; if there is motion - status = 1
    status = 0
    # Converts color frame to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blurs and updates the gray image
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnt, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Detects if contours are less than 10000; if so, the status changes to 1 detecting movement in the frame
    for contour in cnt:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    status_list.append(status)

    # Records the time that the status changes from 0 to 1
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    # Records the time that the status changes from 1 to 0
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Show the gray scale images
    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    # Press any button to close the window
    key = cv2.waitKey(1)

    # stops script if 'q' is pressed
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

end = None
if len(times) % 2!= 0:
    end = len(times) -1
else:
    end = len(times)

for i in range(0, end, 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

df.to_csv("Times.csv")
# Release the camera/video
video.release()
# Destroys all open windows.
cv2.destroyAllWindows()
