import cv2
import numpy as np

img = cv2.imread( r"C:\Users\DELL\Documents\computer vision lab\images (1).jpeg")

if img is None:
    print("Image not found!")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    background = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original Image", img)
    cv2.imshow("Extracted Background Color", background)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
