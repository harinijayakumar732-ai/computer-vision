import cv2

cap = cv2.VideoCapture(r"C:\Users\DELL\Downloads\27180-362142275.mp4")

frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

if len(frames) == 0:
    print("Video not found or no frames available!")
else:
    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
