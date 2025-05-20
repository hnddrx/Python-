import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define filter modes
FILTERS = ["Normal", "Grayscale", "Edge Detection", "Sketch", "Cartoon"]
filter_mode = 0  # Start with "Normal" mode

def apply_filter(frame, mode):
    if mode == 1:  # Grayscale
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 2:  # Edge Detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    elif mode == 3:  # Sketch (Pencil Sketch Effect)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        inv_gray = 255 - gray
        blurred = cv2.GaussianBlur(inv_gray, (21, 21), 0)
        sketch = cv2.divide(gray, 255 - blurred, scale=256)
        return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    elif mode == 4:  # Cartoon Effect
        # Downsample image for faster processing
        img_color = cv2.pyrDown(frame)
        for _ in range(2):  # Repeatedly apply bilateral filter
            img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=75, sigmaSpace=75)
        img_color = cv2.pyrUp(img_color)
        
        # Convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)
        
        # Edge detection
        edges = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        # Combine color and edges
        cartoon = cv2.bitwise_and(img_color, edges)
        return cartoon
    return frame

print("Press 'f' to switch filters. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the selected filter
    filtered_frame = apply_filter(frame, filter_mode)

    # Show the filter mode name on the screen
    filter_name = FILTERS[filter_mode]
    cv2.putText(filtered_frame, f"Filter: {filter_name}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the filtered frame
    cv2.imshow("Real-Time Filter Effects", filtered_frame)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF
    if key == ord('f'):  # Press 'f' to switch filters
        filter_mode = (filter_mode + 1) % len(FILTERS)
    elif key == ord('q'):  # Press 'q' to quit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
