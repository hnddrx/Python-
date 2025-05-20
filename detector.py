import cv2
import os

config_path = r"C:\Playground\python\MobileNetSSD_deploy.prototxt"
model_path = r"C:\Playground\python\MobileNetSSD_deploy.caffemodel"

# Confirm paths
assert os.path.isfile(config_path), "Config file not found"
assert os.path.isfile(model_path), "Model file not found"

# Load the network
net = cv2.dnn.readNetFromCaffe(config_path, model_path)

# List of object classes that the model can detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat", 
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", 
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep", 
           "sofa", "train", "tvmonitor"]

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize the frame to fit the model's expected input size and prepare it
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections
    for i in range(detections.shape[2]):
        # Get confidence of prediction
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > 0.2:  # adjust this threshold as needed
            # Extract the index of the class label and compute bounding box
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            # Draw the bounding box and label on the frame
            label = f"{CLASSES[idx]}: {confidence * 100:.2f}%"
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the output frame
    cv2.imshow("Object Detection", frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
