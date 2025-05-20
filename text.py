import cv2
import pytesseract
from PIL import Image
import numpy as np

# Optional: Specify path to tesseract executable (Windows only)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_text_from_camera():
    cap = cv2.VideoCapture(0)  # Open the default camera

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 's' to scan text or 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Camera - Press 's' to scan", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Convert frame to grayscale for better OCR accuracy
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Optional: Apply thresholding or denoising if needed
            # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            # Convert OpenCV image to PIL format
            pil_image = Image.fromarray(gray)

            # Perform OCR using Tesseract
            text = pytesseract.image_to_string(pil_image)

            print("\n--- Detected Text ---")
            print(text.strip())

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_text_from_camera()
