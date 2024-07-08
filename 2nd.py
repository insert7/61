#Operations on 2d object
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame and OpenGL settings
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(1, 1, 1, 1)  # Set background color to white
gluOrtho2D(0, display[0], 0, display[1])  # Set 2D orthographic projection

def draw_triangle(x, y, angle, scale):
    # Apply transformations and draw a triangle
    glPushMatrix()
    glTranslatef(x, y, 0)  # Translate to (x, y)
    glRotatef(angle, 0, 0, 1)  # Rotate around z-axis
    glScalef(scale, scale, 1)  # Scale the triangle
    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 1)  # Set color to blue
    glVertex2f(0, 50)  # Top vertex
    glVertex2f(-50, -50)  # Bottom left vertex
    glVertex2f(50, -50)  # Bottom right vertex
    glEnd()
    glPopMatrix()

# Initial properties of the triangle
tri_x, tri_y = display[0] // 2, display[1] // 2
angle, scale = 0, 1

# Main loop to handle events and render the triangle
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Handle input for translations
    tri_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    tri_y += (keys[pygame.K_UP] - keys[pygame.K_DOWN]) * 5
    # Handle input for rotations
    angle += (keys[pygame.K_q] - keys[pygame.K_e]) * 5
    # Handle input for scaling
    scale += (keys[pygame.K_w] - keys[pygame.K_s]) * 0.1
    scale = max(scale, 0.1)  # Prevent the scale from becoming too small

    glClear(GL_COLOR_BUFFER_BIT)
    draw_triangle(tri_x, tri_y, angle, scale)  # Draw the transformed triangle
    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()