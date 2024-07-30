import cv2 

# Load an image  
image_path = 'image1.png'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale for edge detection 

# Check if image loading was successful 
if img is None: 
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.") 
    exit() 

# Edge Detection using Canny Edge Detector 
edges = cv2.Canny(img, 100, 200)  # Adjust thresholds as needed 

# Texture Filtering using Gaussian Blur 
blurred_img = cv2.GaussianBlur(img, (5, 5), 0) 

# Displaying the results 
cv2.imshow("Original Image", img) 
cv2.imshow("Edges Detected", edges) 
cv2.imshow("Blurred Image", blurred_img)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()