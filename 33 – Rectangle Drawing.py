import cv2

img = cv2.imread(r"C:\Users\DELL\Documents\computer vision lab\vehicle.jpeg")

if img is None:
    print("Image not found!")
else:
    cv2.rectangle(img, (100, 100), (400, 300),
                  (0, 255, 0), 3)

    cv2.imshow("Rectangle Drawing", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
