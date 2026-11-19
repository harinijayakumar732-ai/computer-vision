import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

cap = cv2.VideoCapture(
    r"C:\Users\DELL\Videos\Captures\MediConnect 2026-08-31 09-57-30.mp4"
)

if not cap.isOpened():
    print("Video not found!")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray)

        if text.strip():
            print("Extracted Text:")
            print(text)

        cv2.imshow("Text Extraction from Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
