import cv2
import numpy as np

image_path = 'image1.png'
img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contoured_image = img.copy()
cv2.drawContours(contoured_image, contours, -1, (255, 255, 0), 2)  # -1 signifies drawing all contours

cv2.imshow("Contoured Image", contoured_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
