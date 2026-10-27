
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found")
    exit()

kernel = np.ones((5, 5), np.uint8)

dilated = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Morphological Image Dilation", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
