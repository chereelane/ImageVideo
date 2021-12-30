import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# read image
img = cv2.imread("photo.jpg")

# create grayscale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detects x,y,w,h on a photo
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.05,
                                      minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
print(type(faces))
print(faces)

# Resizing the photos
resized = cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))
# Displays the image and waits for any key for image to disappear
cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
