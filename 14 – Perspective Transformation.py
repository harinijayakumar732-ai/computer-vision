
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found")
    exit()

rows, cols = img.shape[:2]

src_points = np.float32([
    [0, 0],
    [cols - 1, 0],
    [0, rows - 1],
    [cols - 1, rows - 1]
])

dst_points = np.float32([
    [50, 50],
    [cols - 50, 0],
    [0, rows - 50],
    [cols - 1, rows - 1]
])

matrix = cv2.getPerspectiveTransform(src_points, dst_points)

transformed = cv2.warpPerspective(img, matrix, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
