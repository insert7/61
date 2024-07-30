import cv2

# Load an image
image_path = 'image1.png'
img = cv2.imread(image_path)

# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

# Apply Gaussian Blur
blurred_img_gaussian = cv2.GaussianBlur(img, (11, 11), 0)  # Kernel size (11, 11), sigma = 0

# Apply Median Blur
blurred_img_median = cv2.medianBlur(img, 5)  # Kernel size 5x5

# Display the original image and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", blurred_img_gaussian)
cv2.imshow("Median Blur", blurred_img_median)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()