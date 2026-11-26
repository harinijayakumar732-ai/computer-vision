import cv2
import numpy as np

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

dilated = cv2.dilate(binary, kernel, iterations=1)

cv2.imshow("Original Image", gray)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
