import cv2
import numpy as np

def order_points(pts):
    """Orders points in clockwise order."""
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    
    return rect

def four_point_transform(image, pts):
    """Applies a perspective transform to the given points."""
    rect = order_points(pts)
    (tl, tr, br, bl) = rect
    
    # Compute width and height of new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    
    # Define destination points
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    
    # Perspective transform
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
    return warped

# Initialize camera
cap = cv2.VideoCapture(0)
print("Adjust the document in front of the camera. Press 's' to scan, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for easier processing
    ratio = frame.shape[0] / 500.0
    orig = frame.copy()
    frame = cv2.resize(frame, (int(frame.shape[1] / ratio), 500))
    
    # Convert to grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Edge detection
    edged = cv2.Canny(gray, 75, 200)
    
    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
    
    # Loop over contours to find the document
    doc_cnt = None
    for c in contours:
        # Approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        
        # If approximated contour has four points, it might be our document
        if len(approx) == 4:
            doc_cnt = approx
            break
    
    # If document contour is found, apply the perspective transformation
    if doc_cnt is not None:
        warped = four_point_transform(orig, doc_cnt.reshape(4, 2) * ratio)
        warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        _, scanned = cv2.threshold(warped_gray, 127, 255, cv2.THRESH_BINARY)
        
        # Show the scanned document
        cv2.imshow("Scanned Document", scanned)
    
    # Show the edges and original frame
    cv2.imshow("Original", frame)
    cv2.imshow("Edges", edged)
    
    # Save the scanned document when 's' is pressed
    if cv2.waitKey(1) & 0xFF == ord('s') and doc_cnt is not None:
        cv2.imwrite("scanned_document.png", scanned)
        print("Document saved as 'scanned_document.png'.")

    # Quit when 'q' is pressed
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
