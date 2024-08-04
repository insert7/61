import cv2
image_path = 'image1.png'
img = cv2.imread(image_path)

blurred_img_gaussian = cv2.GaussianBlur(img, (11, 11), 0) 

blurred_img_median = cv2.medianBlur(img, 5) 

cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur", blurred_img_gaussian)
cv2.imshow("Median Blur", blurred_img_median)

cv2.waitKey(0)
cv2.destroyAllWindows()
