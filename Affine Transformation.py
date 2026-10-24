
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found")
    exit()

rows, cols = img.shape[:2]

src_points = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

dst_points = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

matrix = cv2.getAffineTransform(src_points, dst_points)

transformed = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()
