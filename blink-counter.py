import cv2
import dlib
import numpy as np

# Load Dlib's pre-trained face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Define the EAR threshold for blink detection
EAR_THRESHOLD = 0.2  # You may need to adjust this for your camera/environment
CONSECUTIVE_FRAME_THRESHOLD = 3  # Minimum number of frames for a blink to be counted

# Define the indices for the left and right eyes based on the 68 facial landmarks
LEFT_EYE_POINTS = list(range(36, 42))  # Left eye landmarks (36-41)
RIGHT_EYE_POINTS = list(range(42, 48))  # Right eye landmarks (42-47)

# Function to calculate the Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye_points, shape):
    # Get the coordinates of the eye landmarks
    eye = np.array([(shape.part(i).x, shape.part(i).y) for i in eye_points])

    # Calculate the Euclidean distances
    A = np.linalg.norm(eye[1] - eye[5])  # Vertical distance between P2 and P6
    B = np.linalg.norm(eye[2] - eye[4])  # Vertical distance between P3 and P5
    C = np.linalg.norm(eye[0] - eye[3])  # Horizontal distance between P1 and P4

    # EAR formula
    ear = (A + B) / (2.0 * C)
    return ear

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Blink counter and flag to track blink detection
blink_counter = 0
blink_detected = False
prev_ear = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)

    for face in faces:
        # Detect facial landmarks
        landmarks = predictor(gray, face)

        # Calculate EAR for both eyes
        left_eye_ear = eye_aspect_ratio(LEFT_EYE_POINTS, landmarks)
        right_eye_ear = eye_aspect_ratio(RIGHT_EYE_POINTS, landmarks)

        # Average EAR of both eyes
        ear = (left_eye_ear + right_eye_ear) / 2.0

        # If EAR is below the threshold, count as closed eye
        if ear < EAR_THRESHOLD:
            blink_counter += 1
            if blink_counter >= CONSECUTIVE_FRAME_THRESHOLD:
                if not blink_detected:
                    blink_detected = True
                    print("Blink detected!")
        else:
            if blink_counter >= CONSECUTIVE_FRAME_THRESHOLD:
                blink_counter = 0
            blink_detected = False

        # Display EAR on the frame
        cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Draw landmarks on face (optional)
        for i in range(36, 48):  # Draw eyes landmarks (36 to 47)
            cv2.circle(frame, (landmarks.part(i).x, landmarks.part(i).y), 1, (0, 0, 255), -1)

    # Display the frame
    cv2.putText(frame, f"Blinks: {blink_counter}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Eye Blink Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()
