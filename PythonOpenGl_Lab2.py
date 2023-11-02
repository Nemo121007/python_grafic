import pygame 
from pygame.locals import * 
from OpenGL.GL import * 
from OpenGL.GLU import *
def Cube(verticesCube, surfacesCube, colorsCube):

    glBegin(GL_QUADS)
    x=0
    for surface in surfacesCube:
        for vertex in surface:
            glColor3fv(colorsCube[x])
            glVertex3fv(verticesCube[vertex])
        x+=1
    glEnd()

def Tr():

    # Передняя стенка
    glBegin(GL_TRIANGLES)
    glColor(1, 0, 0)
    glVertex3f(3.0, -1.0, 1.0)
    glColor(0, 1, 0)
    glVertex3f(5.0, -1.0, 1.0)
    glColor(0, 0, 1)
    glVertex3f(4.0, 1.0, 0.0)
    glEnd()

    # Праваая стенка
    glBegin(GL_TRIANGLES)
    glColor(0, 1, 0)
    glVertex3f(5.0, -1.0, 1.0)
    glColor(1, 0, 0)
    glVertex3f(5.0, -1.0, -1.0)
    glColor(0, 0, 1)
    glVertex3f(4.0, 1.0, 0.0)
    glEnd()

    # Задняя стенка
    glBegin(GL_TRIANGLES)
    glColor(1, 0, 0)
    glVertex3f(5.0, -1.0, -1.0)
    glColor(0, 1, 0)
    glVertex3f(3.0, -1.0, -1.0)
    glColor(0, 0, 1)
    glVertex3f(4.0, 1.0, 0.0)
    glEnd()

    # Левая стенка
    glBegin(GL_TRIANGLES)
    glColor(0, 1, 0)
    glVertex3f(3.0, -1.0, -1.0)
    glColor(1, 0, 0)
    glVertex3f(3.0, -1.0, 1.0)
    glColor(0, 0, 1)
    glVertex3f(4.0, 1.0, 0.0)
    glEnd()

    # Нижняя стенка
    glBegin(GL_QUADS)
    glColor(1, 0, 0)
    glVertex3f(3.0, -1.0, 1.0)
    glColor(0, 1, 0)
    glVertex3f(5.0, -1.0, 1.0)
    glColor(1, 0, 0)
    glVertex3f(5.0, -1.0, -1.0)
    glColor(0, 1, 0)
    glVertex3f(3.0, -1.0, -1.0)
    glEnd()

def main():
    verticesCube=(
        (1.0, -1.0, -1.0),
        (1.0, 1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (1.0, -1.0, 1.0),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0)
        )

    surfacesCube = (
        (0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6)
        )
    colorsCube = (
        (1, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 1),
        )

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
        Cube(verticesCube, surfacesCube, colorsCube)
        Tr()
        pygame.display.flip()
        pygame.time.wait(1)
main()