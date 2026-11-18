import cv2

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\images.jpeg")

if img is None:
    print("Image not found!")
else:
    cv2.circle(img, (250, 200), 80, (255, 0, 0), 3)

    cv2.imshow("Circle Drawing", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
