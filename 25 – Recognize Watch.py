
import cv2

img = cv2.imread(
    r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg"
)

if img is None:
    print("Image not found")
    exit()

cv2.imshow("Watch Recognition - Input Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
