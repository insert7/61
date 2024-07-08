#Operations on 3d object
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the vertices of a cube
vertices = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
            (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]

# Define the edges of the cube by connecting vertices
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), 
         (0, 4), (1, 5), (2, 6), (3, 7)]

# Define the surfaces (or faces) of the cube by connecting vertices
surfaces = [(0, 1, 2, 3), (3, 2, 6, 7), (7, 6, 5, 4), (4, 5, 1, 0),
            (1, 5, 6, 2), (4, 0, 3, 7)]

# Define colors for each surface of the cube
colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1)]

def draw_cube():
    # Draw the cube with colors
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

# Initialize Pygame and OpenGL settings
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(1, 1, 1, 1)  # Set background color to white
glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D rendering
gluPerspective(45, display[0] / display[1], 0.1, 50.0)  # Set perspective projection
glTranslatef(0, 0, -5)  # Move the camera back

# Initial transformations
translate, rotate, scale = [0, 0, 0], [0, 0, 0], 1

# Main loop to handle events and render the cube
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # Handle input for translations
    translate[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 0.05
    translate[1] += (keys[pygame.K_UP] - keys[pygame.K_DOWN]) * 0.05
    # Handle input for rotations
    rotate[0] += keys[pygame.K_x] * 3
    rotate[1] += keys[pygame.K_y] * 3
    rotate[2] += keys[pygame.K_z] * 3
    # Handle input for scaling
    scale += (keys[pygame.K_w] - keys[pygame.K_s]) * 0.05
    scale = max(scale, 0.05)  # Prevent the scale from becoming too small

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    # Apply transformations
    glTranslatef(*translate)
    glScalef(scale, scale, scale)
    glRotatef(rotate[0], 1, 0, 0)
    glRotatef(rotate[1], 0, 1, 0)
    glRotatef(rotate[2], 0, 0, 1)
    draw_cube()  # Draw the transformed cube
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()