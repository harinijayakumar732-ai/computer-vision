import cv2

img = cv2.imread( r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")

if img is None:
    print("Image not found!")
else:
    cv2.putText(
        img, "Computer Vision",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 2
    )

    cv2.imshow("Text on Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
