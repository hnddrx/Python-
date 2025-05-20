import cv2
import mediapipe as mp
import time
import ctypes


# Initialize MediaPipe and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]  # Thumb and fingers tip landmarks

def fingers_up(hand_landmarks):
    fingers = []

    # Thumb (check x for left/right based on handedness)
    if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[tip_ids[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Fingers (check y to determine up/down)
    for id in range(1, 5):
        if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

screenshot_taken = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_status = fingers_up(hand_landmarks)
            total_fingers = sum(finger_status)

            # Show number of fingers up
            cv2.putText(frame, f'Fingers up: {total_fingers}', (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Take screenshot if exactly 2 fingers are up
            # Take screenshot if exactly 2 fingers are up
            if total_fingers == 0 and not screenshot_taken:
                timestamp = int(time.time())
                filename = f'C:/Users/macayan_w/Downloads/screenshot_{timestamp}.png'
                cv2.imwrite(filename, frame)
                print(f'[INFO] Screenshot saved to: {filename}')
                screenshot_taken = True
                """ elif total_fingers == 1:
                    print("[INFO] One finger detected — locking the device...")
                    ctypes.windll.user32.LockWorkStation()
                    break  # Optional: stop the script after locking """
            elif total_fingers != 0:
                screenshot_taken = False


    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
