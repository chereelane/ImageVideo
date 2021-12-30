import cv2
import glob

# This script resizes all the images to 100x100 in a given directory

# get directory
images = glob.glob("*.jpg")

# for all images in the given directory resize images
for image in images:
    img = cv2.imread(image, 0)
    resize = cv2.resize(img, (100, 100))
    cv2.imshow("Done", resize)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image, resize)

