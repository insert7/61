import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Square properties
position = [0.5, 0.0]
speed = [0.005, 0.005]
size = 0.05

def draw_square():
    glColor3f(0, 0, 0) # set color to green
    glBegin(GL_QUADS) # start drawing a square
    glVertex2f(-size, -size) # bottom left point
    glVertex2f(size, -size) # bottom right point
    glVertex2f(size, size) # top right point
    glVertex2f(-size, size) # top left point
    glEnd() # done drawing a square

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Simple Square Animation")

    gluOrtho2D(-1, 1, -1, 1) # set coordinate system from -1 to 1 in both axes
    glClearColor(1, 1, 1, 1) # set background color to red


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Update square position
        position[0] -= speed[0]
        position[1] -= speed[1]

        # Check for collision with walls and bounce
        if abs(position[0]) > 1 - size:
            speed[0] *= -1
        if abs(position[1]) > 1 - size:
            speed[1] *= -1

        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix() # save the current transformation
        glTranslate(position[0], position[1], 0) # move to the square's position
        draw_square() # draw the square
        glPopMatrix() # restore the previous transformation
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()