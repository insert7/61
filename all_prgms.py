import matplotlib.pyplot as plt
def draw_line(x0, y0, x1, y1):
    # Calculate dx and dy
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    # Calculate the direction of the line
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    if y0 < y1:
        sy = 1
    else:
        sy = -1
    # Initialize the error
    error = dx - dy
    # Initialize the current position
    x = x0
    y = y0
    # Draw the line
    line = []
    while True:
        # Add the current point to the line
        line.append((x, y))
        # Check if the end point is reached
        if x == x1 and y == y1:
            break
        # Calculate the next position
        e2 = 2 * error
        if e2 > -dy:
            error -= dy
            x += sx
        if e2 < dx:
            error += dx
            y += sy
    return line
# Example usage
x0, y0 = 1, 1
x1, y1 = 4, 4
line = draw_line(x0, y0, x1, y1)
# Plotting the line
x_values = [point[0] for point in line]
y_values = [point[1] for point in line]
plt.plot(x_values, y_values, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Bresenham Line Drawing')
plt.grid(True)
plt.show()


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Initialize Pygame and set up an OpenGL display
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(1, 1, 1, 1)  # Set background color to white
# Set up the view
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, display[0], 0, display[1])
glMatrixMode(GL_MODELVIEW)
# Triangle properties
tri_x, tri_y = display[0] // 2, display[1] // 2
angle = 0
scale = 1
def draw_triangle(x, y, angle, scale):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glScalef(scale, scale, 1.0)
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(0, 50)  # Top vertex
    glVertex2f(-50, -50)  # Bottom left vertex
    glVertex2f(50, -50)  # Bottom right vertex
    glEnd()
    glPopMatrix()
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        tri_x -= 5  # Translate left
    if keys[pygame.K_RIGHT]:
        tri_x += 5  # Translate right
    if keys[pygame.K_UP]:
        tri_y += 5  # Translate up
    if keys[pygame.K_DOWN]:
        tri_y -= 5  # Translate down
    if keys[pygame.K_q]:
        angle += 5  # Rotate counter-clockwise
    if keys[pygame.K_e]:
        angle -= 5  # Rotate clockwise
    if keys[pygame.K_w]:
        scale += 0.1  # Scale up
    if keys[pygame.K_s]:
        scale -= 0.1  # Scale down
    if scale < 0.1:
        scale = 0.1
    glClear(GL_COLOR_BUFFER_BIT)
    draw_triangle(tri_x, tri_y, angle, scale)
    pygame.display.flip()
    pygame.time.wait(30)
pygame.quit()


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (-1, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 6, 7),
    (7, 6, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 6, 2),
    (4, 0, 3, 7)
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1)
)

def Cube():
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    clock = pygame.time.Clock()

    translate = [0, 0, 0]
    rotate = [0, 0, 0]
    scale = 1
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            translate[0] -= 0.05
        if keys[pygame.K_RIGHT]:
            translate[0] += 0.05
        if keys[pygame.K_UP]:
            translate[1] += 0.05
        if keys[pygame.K_DOWN]:
            translate[1] -= 0.05
        if keys[pygame.K_x]:
            rotate[0] += 3
        if keys[pygame.K_z]:
            rotate[2] += 3
        if keys[pygame.K_y]:
            rotate[1] += 3
        if keys[pygame.K_w]:
            scale += 0.05
        if keys[pygame.K_s]:
            scale -= 0.05

        if scale < 0.05:
            scale = 0.05

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glTranslatef(*translate)
        glScalef(scale, scale, scale)
        glRotatef(rotate[0], 1, 0, 0)
        glRotatef(rotate[1], 0, 1, 0)
        glRotatef(rotate[2], 0, 0, 1)
        Cube()
        glPopMatrix()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()


import pygame
import sys

def main():
    pygame.init()
        
    screen_width = 800
    screen_height = 600

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    ball_pos = [screen_width // 2, screen_height // 2]
    ball_radius = 20 
    ball_speed = [2, 2]

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simple Ball Animation")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        if ball_pos[0] - ball_radius < 0 or ball_pos[0] + ball_radius > screen_width:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] - ball_radius < 0 or ball_pos[1] + ball_radius > screen_height:
            ball_speed[1] = -ball_speed[1]

        screen.fill(white)

        pygame.draw.circle(screen, red, ball_pos, ball_radius)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()



import cv2
import numpy as np

img = cv2.imread('input_image.jpg')
h, w = img.shape[:2]

ra = 45
rm= cv2.getRotationMatrix2D((w/2, h/2), ra, 1)
ri = cv2.warpAffine(img,rm, (w, h))

sp= 70 
nw = int(w * sp / 100)
nh = int(h * sp / 100)
si = cv2.resize(img, (nw, nh), interpolation=cv2.INTER_LINEAR)

tm = np.float32([[1, 0, 100], [0, 1, 50]])
ti = cv2.warpAffine(img, tm, (w, h))

cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', ri)
cv2.imshow('Scaled Image', si)
cv2.imshow('Translated Image', ti)

cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
import numpy as np

# Function to display an image with OpenCV
def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load an image
image_path = 'snow.jpg'
image=cv2.imread(image_path)
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) # Load as grayscale for edge detection
# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

# Edge Detection using Canny Edge Detector
edges = cv2.Canny(img, 100, 200) # Adjust thresholds as needed

# Texture Filtering using Gaussian Blur
blurred_img = cv2.GaussianBlur(img, (5, 5), 0)

# Displaying the results
display_image(image, "Original Image")
display_image(edges, "Edges Detected")
display_image(blurred_img, "Blurred Image")


import cv2

# Function to display an image
def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Path to the image
image_path = 'snow.jpg'
# Load the image
img = cv2.imread(image_path)
# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()
# Apply Gaussian Blur
blurred_img_gaussian = cv2.GaussianBlur(img, (11, 11), 0)  # Kernel size (11, 11), sigma = 0
# Apply Median Blur
blurred_img_median = cv2.medianBlur(img, 5)  # Kernel size 5x5
# Apply Bilateral Filter
blurred_img_bilateral = cv2.bilateralFilter(img, 9, 75, 75)  # Diameter, sigmaColor, sigmaSpace
# Apply Box Filter (Smoothing)
blurred_img_box = cv2.blur(img, (10, 10))  # Kernel size (10, 10)
# Display the original image and blurred images
display_image(img, "Original Image")
display_image(blurred_img_gaussian, "Gaussian Blur")
display_image(blurred_img_median, "Median Blur")
display_image(blurred_img_bilateral, "Bilateral Filter")
display_image(blurred_img_box, "Box Filter (Smoothing)")



import cv2
import numpy as np

# Function to display an image with OpenCV
def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load an image
image_path = 'snow.jpg'
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
cv2.drawContours(contoured_image, contours, -1, (0, 255, 0), 2) # -1 signifies drawing all contours

# Display the original image with contours
display_image(img, "Original Image")
display_image(contoured_image, "Contoured Image")



import cv2

# Function to display an image with OpenCV
def display_image(image, title="Image"):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image
image_path = 'hugh.jpg'
img = cv2.imread(image_path)
    
# Check if image loading was successful
if img is None:
    print(f"Error: Unable to load image '{image_path}'. Please check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the image with detected faces
display_image(img, "Detected Faces")
