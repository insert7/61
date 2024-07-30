import cv2
import numpy as np

# Load an image
image_path = 'image.png'
img = cv2.imread(image_path)

# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Face Detected', img)
cv2.waitKey(0)
cv2.destroyAllWindows()