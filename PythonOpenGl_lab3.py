import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Cylinder(circle, height):
    glColor(0, 0, 1)
    glVertex3f(0, height, 0)
    glColor(0, 0, 1)
    glVertex3f(0, -height, 0)

    for i in range(len(circle) - 1):
        glBegin(GL_TRIANGLES)
        glColor(1, 0, 0)
        glVertex3f(circle[i][0], circle[i][1], height)
        glVertex3f(circle[i + 1][0], circle[i + 1][1], height)
        glColor(0, 0, 1)
        glVertex3f(0, 0, height)
        glEnd()

        glBegin(GL_TRIANGLES)
        glColor(0, 1, 0)
        glVertex3f(circle[i][0], circle[i][1], -height)
        glVertex3f(circle[i + 1][0], circle[i + 1][1], -height)
        glColor(0, 0, 1)
        glVertex3f(0, 0, -height)
        glEnd()

        glBegin(GL_QUADS)
        glColor(i, 255 - i % 2, 0)
        glColor(1, 0, 0)
        glVertex3f(circle[i][0], circle[i][1], height)
        glColor(0, 1, 0)
        glVertex3f(circle[i][0], circle[i][1], -height)
        glVertex3f(circle[i + 1][0], circle[i + 1][1], -height)
        glColor(1, 0, 0)
        glVertex3f(circle[i + 1][0], circle[i + 1][1], height)
        glEnd()

def Round(radius, number):
    circle_pts = []
    for i in range(number + 1):
        angle = 2 * math.pi * (i / number)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)
    return circle_pts

def main():

    radius = 1
    height = 1
    height = height / 2
    number = 30
    circle = Round(radius, number)

    pygame.init()
    display=(1200,700)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluPerspective(40, (display[0]/display[1]), 1.0, 50.0)
    glTranslatef(0.0, 0.0, -8)
    glRotatef(30, 1, 1, 1)
    glEnable(GL_DEPTH_TEST)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(0.1, 1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cylinder(circle, height)
        pygame.display.flip()
        pygame.time.wait(1)
main()
