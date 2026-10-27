
import cv2

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found")
    exit()

h, w = img.shape[:2]

# Crop a Region of Interest (ROI)
roi_h = max(1, h // 4)
roi_w = max(1, w // 4)

y = (h - roi_h) // 2
x = (w - roi_w) // 2

roi = img[y:y + roi_h, x:x + roi_w].copy()

# Copy the ROI to the top-left corner
result = img.copy()
result[0:roi_h, 0:roi_w] = roi

cv2.imshow("Original Image", img)
cv2.imshow("Cropped ROI", roi)
cv2.imshow("Image with ROI Pasted", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
