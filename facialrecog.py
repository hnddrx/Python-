import cv2
from fer import FER

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initialize the emotion detector
detector = FER(mtcnn=True)  # Use MTCNN for better face detection

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert frame from BGR (OpenCV) to RGB (FER expects RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect emotions in the frame
    results = detector.detect_emotions(rgb_frame)

    for result in results:
        (x, y, w, h) = result["box"]

        # Extract face region (in RGB)
        face = rgb_frame[y:y+h, x:x+w]

        # Get top emotion for the face
        top_emotion = detector.top_emotion(face)
        if top_emotion is None:
            continue
        emotion, score = top_emotion

        # Draw rectangle on original BGR frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        label = f"{emotion} ({score:.2f})"
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 0), 2)

    cv2.imshow("Facial Emotion Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
