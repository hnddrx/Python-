import cv2
import mediapipe as mp
import math

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define a function to calculate Euclidean distance
def calc_distance(point1, point2):
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

# Approximate reference: pixel distance of 0.15 (normalized) ~ 2.5 inches (thumb to index at full stretch)
reference_pixel_distance = 0.15
reference_inch_distance = 2.5

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        h, w, _ = frame.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Thumb tip = 4, Index tip = 8
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Draw circles
                thumb_coords = (int(thumb_tip.x * w), int(thumb_tip.y * h))
                index_coords = (int(index_tip.x * w), int(index_tip.y * h))

                cv2.circle(frame, thumb_coords, 8, (255, 0, 0), -1)
                cv2.circle(frame, index_coords, 8, (0, 255, 0), -1)
                cv2.line(frame, thumb_coords, index_coords, (0, 0, 255), 2)

                # Calculate normalized distance
                norm_dist = calc_distance(thumb_tip, index_tip)

                # Convert to inches
                inches = (norm_dist / reference_pixel_distance) * reference_inch_distance
                text = f"Distance: {inches:.2f} in"

                # Show on frame
                cv2.putText(frame, text, (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (50, 50, 255), 2)

        cv2.imshow("Hand Ruler (Inches)", frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
