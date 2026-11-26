import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

img = np.ones((height, width, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (0, 0), (100, 100), (0, 0, 255), -1)
cv2.rectangle(img, (width-100, 0), (width-1, 100), (0, 255, 0), -1)
cv2.rectangle(img, (0, height-100), (100, height-1), (255, 0, 0), -1)
cv2.rectangle(img, (width-100, height-100), (width-1, height-1), (0, 255, 255), -1)

cv2.imshow("Four Colored Rectangles", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
