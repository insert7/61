import cv2

# 1. Load the image and get its dimensions
image = cv2.imread('image1.png')
height, width, channels = image.shape

# 2. Calculate the center coordinates of the image
center_y = height // 2
center_x = width // 2

# 3. Split the image into four quadrants
top_left = image[0:center_y, 0:center_x]
top_right = image[0:center_y, center_x:width]
bottom_left = image[center_y:height, 0:center_x]
bottom_right = image[center_y:height, center_x:width]

# 4. Display each quadrant in a separate window
cv2.imshow('Top Left', top_left)
cv2.imshow('Top Right', top_right)
cv2.imshow('Bottom Left', bottom_left)
cv2.imshow('Bottom Right', bottom_right)

# 5. Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
