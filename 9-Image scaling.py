
import cv2

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found")
    exit()

# Increase image size
large = cv2.resize(
    img, None, fx=2, fy=2,
    interpolation=cv2.INTER_LINEAR
)

# Decrease image size
small = cv2.resize(
    img, None, fx=0.5, fy=0.5,
    interpolation=cv2.INTER_AREA
)

cv2.imshow("Original Image", img)
cv2.imshow("Scaled Up Image", large)
cv2.imshow("Scaled Down Image", small)

cv2.waitKey(0)
cv2.destroyAllWindows()
