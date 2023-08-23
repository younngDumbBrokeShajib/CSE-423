from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    #glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_LINES) #for base and 2 corners
    glVertex2f(100,0)#base
    glVertex2f(300, 0)
    glVertex2f(300, 0)#right corner
    glVertex2f(300, 200)
    glVertex2f(300, 200)#roof
    glVertex2f(100, 200)
    glVertex2f(100, 200)#left corner
    glVertex2f(100, 0)
    glEnd()


    glBegin(GL_QUADS) #for windows
    glVertex2f(280,85)
    glVertex2f(280, 100)
    glVertex2f(260, 100)
    glVertex2f(260, 85)
    glEnd()

    glBegin(GL_QUADS)#for left window
    glVertex2f(120, 85)
    glVertex2f(140, 85)
    glVertex2f(140, 100)
    glVertex2f(120, 100)
    glEnd()


    glBegin(GL_QUADS) #doors
    glVertex2f(150,0)
    glVertex2f(200, 0)
    glVertex2f(200, 75)
    glVertex2f(150, 75)
    glEnd()

    glBegin(GL_TRIANGLES)# roof er uporer tirangle
    glVertex2f(100,200)
    glVertex2f(300, 200)
    glVertex2f(200, 300)
    glEnd()

    glBegin(GL_POINTS)
    glVertex2f(100, 0)
    glEnd()



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(100.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    draw_points(0, 0)
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
