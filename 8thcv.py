import cv2
import numpy as np

# 1. Load the image
image = cv2.imread('image1.png')

# 2. Rotate the image
angle = 45  # Rotate the image 45 degrees
center = (image.shape[1] // 2, image.shape[0] // 2)  # Image center
rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)  # Scale = 1.0
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# 3. Scale the image
scale_percent = 50  # Scale the image to 25% of its size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
scaled_image = cv2.resize(image, dim)

# 4. Translate the image
tx, ty = 100, 150  # Translate the image 100 pixels right and 50 pixels down
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))

# 5. Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Scaled Image', scaled_image)
cv2.imshow('Translated Image', translated_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
