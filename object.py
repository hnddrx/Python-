# Install required packages if not already installed:
# pip install opencv-python mediapipe ultralytics

import cv2
import mediapipe as mp
from ultralytics import YOLO
import math

# Load YOLOv8 model (you can use yolov8n.pt or yolov8s.pt for speed)
model = YOLO("yolov8n.pt")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Reference real-world distance between thumb tip and index tip in inches (approx)
REFERENCE_HAND_DISTANCE_INCHES = 2.5

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip and convert the frame to RGB
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect hand landmarks
    results = hands.process(rgb_frame)
    hand_distance_pixels = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of thumb tip (landmark 4) and index finger tip (landmark 8)
            h, w, _ = frame.shape
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]

            x1, y1 = int(thumb_tip.x * w), int(thumb_tip.y * h)
            x2, y2 = int(index_tip.x * w), int(index_tip.y * h)

            hand_distance_pixels = math.hypot(x2 - x1, y2 - y1)

            cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.putText(frame, f"{hand_distance_pixels:.1f}px", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    # Run object detection
    results_yolo = model(rgb_frame, verbose=False)[0]
    
    if hand_distance_pixels:
        pixels_per_inch = hand_distance_pixels / REFERENCE_HAND_DISTANCE_INCHES

        for result in results_yolo.boxes:
            x1, y1, x2, y2 = map(int, result.xyxy[0])
            label = model.names[int(result.cls[0])]
            width_pixels = x2 - x1
            height_pixels = y2 - y1

            width_in = width_pixels / pixels_per_inch
            height_in = height_pixels / pixels_per_inch

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)
            cv2.putText(frame,
                        f"{label}: {width_in:.2f}in x {height_in:.2f}in",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)

    cv2.imshow("Hand & Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

