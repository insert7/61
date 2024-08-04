import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
glClearColor(1, 1, 1, 1)  
gluOrtho2D(0, display[0], 0, display[1])

circle_x, circle_y = display[0] // 3, display[1] // 3
angle = 0
scale = 50 

def draw_circle(x, y, radius, num_segments):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0.0, 0.0, 0.0)
    
    glVertex2f(0, 0)
    
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        vx = radius * math.cos(angle)
        vy = radius * math.sin(angle)
        glVertex2f(vx, vy)
    
    glEnd()
    
    glPopMatrix()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        circle_x -= 5 
    if keys[pygame.K_RIGHT]:
        circle_x += 5 
    if keys[pygame.K_UP]:
        circle_y += 5 
    if keys[pygame.K_DOWN]:
        circle_y -= 5 
    if keys[pygame.K_q]:
        angle += 5 
    if keys[pygame.K_e]:
        angle -= 5 
    if keys[pygame.K_w]:
        scale += 3s
    if keys[pygame.K_s]:
        scale -= 3 
        if scale < 0.05: 
            scale = 0.05

    glClear(GL_COLOR_BUFFER_BIT)
    draw_circle(circle_x, circle_y, scale, 30)
    pygame.display.flip()
    pygame.time.wait(30)

pygame.quit()
