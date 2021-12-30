import cv2


img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)


cv2.imshow("Galaxy", img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
