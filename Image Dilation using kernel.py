import cv2
import numpy as np

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found")
    exit()

kernel = np.ones((5, 5), np.uint8)
dil = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Dilated", dil)
cv2.waitKey(0)
cv2.destroyAllWindows()
