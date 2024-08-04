import cv2 

image_path = 'image1.png'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 100, 200)

blurred_img = cv2.GaussianBlur(img, (5, 5), 0) 

cv2.imshow("Original Image", img) 
cv2.imshow("Edges Detected", edges) 
cv2.imshow("Blurred Image", blurred_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
