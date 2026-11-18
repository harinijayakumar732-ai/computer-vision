import cv2

img = cv2.imread( r"C:\Users\DELL\Documents\computer vision lab\sample.jpeg")
watermark = cv2.imread(r"C:\Users\DELL\Downloads\watermarking.jpeg")

if img is None or watermark is None:
    print("Image or watermark not found!")
else:
    watermark = cv2.resize(watermark, (150, 80))

    h, w = watermark.shape[:2]
    roi = img[20:20+h, 20:20+w]

    blended = cv2.addWeighted(roi, 0.6, watermark, 0.4, 0)
    img[20:20+h, 20:20+w] = blended

    cv2.imshow("Watermarked Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
