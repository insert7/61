import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

position = [0.0, 0.0]
speed = [0.01, 0.02]
size = 0.08

def draw_square():
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(-size, -size)
    glVertex2f(size, -size)
    glVertex2f(size, size)
    glVertex2f(-size, size)
    glEnd()

def main():
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF|OPENGL)
    pygame.display.set_caption("Simple Square Animation")

    gluOrtho2D(-1, 1, -1, 1)
    glClearColor(1, 1, 1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        position[0] -= speed[0]
        position[1] -= speed[1]

        if abs(position[0]) > 1 - size:
            speed[0] *= -1
        if abs(position[1]) > 1 - size:
            speed[1] *= -1

        glClear(GL_COLOR_BUFFER_BIT)
        glPushMatrix()
        glTranslate(position[0], position[1], 0)
        draw_square()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
