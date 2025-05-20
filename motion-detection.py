import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize background frame
ret, bg_frame = cap.read()
bg_frame = cv2.cvtColor(bg_frame, cv2.COLOR_BGR2GRAY)
bg_frame = cv2.GaussianBlur(bg_frame, (21, 21), 0)

print("Motion detection activated. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert current frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    # Compute difference between the background and current frame
    diff_frame = cv2.absdiff(bg_frame, gray_frame)
    _, thresh_frame = cv2.threshold(diff_frame, 25, 255, cv2.THRESH_BINARY)

    # Dilate the threshold frame to fill in holes
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Find contours in the threshold frame
    contours, _ = cv2.findContours(thresh_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around moving objects
    for contour in contours:
        if cv2.contourArea(contour) < 1000:  # Ignore small areas
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Motion Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frames
    cv2.imshow("Motion Detector", frame)
    cv2.imshow("Threshold Frame", thresh_frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
