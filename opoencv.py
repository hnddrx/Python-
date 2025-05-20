import cv2
import numpy as np

# Function to count fingers and identify which ones
def count_and_identify_fingers(hand_contour, frame):
    # Find the convex hull of the hand
    hull = cv2.convexHull(hand_contour, returnPoints=False)
    
    # Find the convexity defects
    defects = cv2.convexityDefects(hand_contour, hull)
    
    if defects is None:
        return 0, []  # No fingers detected
    
    finger_count = 0
    detected_fingers = []
    
    # Iterate over each defect
    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(hand_contour[s][0])
        end = tuple(hand_contour[e][0])
        far = tuple(hand_contour[f][0])

        # Calculate the angle between the fingers using the cosine rule
        a = np.linalg.norm(np.array(end) - np.array(start))
        b = np.linalg.norm(np.array(far) - np.array(start))
        c = np.linalg.norm(np.array(end) - np.array(far))
        angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))  # Cosine rule

        # If the angle is less than 90 degrees, we have a finger
        if angle <= np.pi / 2:  # Only count if the angle is small (typically a finger)
            finger_count += 1
            cv2.circle(frame, far, 8, [255, 0, 0], -1)

            # Assign finger names based on position in the hand
            # (This is a simple heuristic to identify fingers)
            if s == 0:
                detected_fingers.append("Thumb")
            elif s == 1:
                detected_fingers.append("Index")
            elif s == 2:
                detected_fingers.append("Middle")
            elif s == 3:
                detected_fingers.append("Ring")
            elif s == 4:
                detected_fingers.append("Little")
    
    # The number of fingers is defects + 1 (since defects count the gaps, not the thumb)
    return finger_count + 1, detected_fingers

# Function to determine if it's a left or right hand
def detect_hand_orientation(hand_contour, frame):
    # Calculate the convex hull and the moments of the contour
    hull = cv2.convexHull(hand_contour)
    M = cv2.moments(hull)
    
    # Calculate the center of the hand's convex hull
    if M["m00"] == 0:
        return "Unknown"
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    
    # Get the frame center (for reference)
    frame_center_x = frame.shape[1] // 2
    
    # Determine if the hand is on the left or right of the frame center
    if cx < frame_center_x:
        return "Left"
    elif cx > frame_center_x:
        return "Right"
    else:
        return "Unknown"

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally to mirror the image (user-friendly for webcam)
    frame = cv2.flip(frame, 1)
    
    # Define region of interest (ROI) for detecting hand (centered region)
    roi = frame[100:400, 100:400]
    
    # Convert ROI to grayscale
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve thresholding
    blurred = cv2.GaussianBlur(gray, (35, 35), 0)

    # Adaptive thresholding to better capture the hand contours
    _, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        # Get the largest contour (assuming the largest contour is the hand)
        hand_contour = max(contours, key=cv2.contourArea)

        # Draw the contour of the hand for visualization
        cv2.drawContours(roi, [hand_contour], -1, (0, 255, 0), 2)
        
        # Count fingers and identify which fingers
        fingers, detected_fingers = count_and_identify_fingers(hand_contour, frame)
        
        # Detect hand orientation (left or right)
        hand_orientation = detect_hand_orientation(hand_contour, frame)
        
        # Display the finger count, names of the detected fingers, and hand orientation
        cv2.putText(frame, f"Fingers: {fingers}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(frame, f"Detected: {', '.join(detected_fingers)}", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Hand: {hand_orientation}", (10, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    
    # Display the thresholded image for debugging (optional)
    cv2.imshow("Thresholded", thresholded)
    cv2.imshow("Finger Count", frame)
    
    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
