import cv2
import numpy as np

# Load an image
image_path = 'image1.png'
img = cv2.imread(image_path)

# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection using Canny
edges = cv2.Canny(blurred, 50, 150)

# Find contours in the edged image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the original image
contoured_image = img.copy()
cv2.drawContours(contoured_image, contours, -1, (255, 255, 0), 2)  # -1 signifies drawing all contours

# Display the original image with contours
cv2.imshow("Contoured Image", contoured_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()