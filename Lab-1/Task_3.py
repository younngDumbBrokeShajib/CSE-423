from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):

    glBegin(GL_POINTS)
    #glVertex2f(100, 0)
    glEnd()

    #showing id - 19101250
    #SETTING MAX HEINGT=200 X-AXIS STARTS FROM 80
    glColor3f(1.0, 2, 0)
    glBegin(GL_LINES)

    # FOR - 1
    glVertex2f(80, 100)
    glVertex2f(80, 200)
    glEnd()

    # FOR - 9
    glColor3f(0.5, 3, 1)
    glBegin(GL_LINES)
    glVertex2f(90, 200)
    glVertex2f(130, 200)
    glVertex2f(130, 200)
    glVertex2f(130, 100)
    glVertex2f(90, 150)
    glVertex2f(90, 200)
    glVertex2f(90, 150)
    glVertex2f(130, 150)
    glVertex2f(90, 100)
    glVertex2f(130, 100)
    glEnd()
    # FOR-1
    glColor3f(3.0, 4.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(140, 200)
    glVertex2f(140, 100)
    glEnd()

    # FOP-0
    glColor3f(2.5, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(160, 200)
    glVertex2f(160, 100)
    glVertex2f(180, 200)
    glVertex2f(180, 100)
    glVertex2f(160, 200)
    glVertex2f(180, 200)
    glVertex2f(160, 100)
    glVertex2f(180, 100)
    glEnd()
    #FOR- 1
    glColor3f(0.0, 0.0, 9.0)
    glBegin(GL_LINES)
    glVertex2f(200, 200)
    glVertex2f(200, 100)
    glEnd()

    #FOR- 2
    glColor3f(0.0, 9.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(220, 200)
    glVertex2f(240, 200)
    glVertex2f(240, 200)
    glVertex2f(240, 150)
    glVertex2f(240, 150)
    glVertex2f(220, 150)
    glVertex2f(220, 150)
    glVertex2f(220, 100)
    glVertex2f(220, 100)
    glVertex2f(240, 100)
    glEnd()

    #FOR 5
    glColor3f(5, 0, 9)
    glBegin(GL_LINES)
    glVertex2f(250, 200)
    glVertex2f(290, 200)
    glVertex2f(290, 150)
    glVertex2f(290, 100)
    glVertex2f(250, 150)
    glVertex2f(250, 200)
    glVertex2f(250, 150)
    glVertex2f(290, 150)
    glVertex2f(250, 100)
    glVertex2f(290, 100)
    glEnd()

    #FOR 0
    glColor3f(7.5, 1.0, 0.5)
    glBegin(GL_LINES)

    glVertex2f(300, 100)
    glVertex2f(320, 100)
    glVertex2f(320, 100)
    glVertex2f(320, 200)
    glVertex2f(320, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 200)
    glVertex2f(300, 100)
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
    #glColor3f(100.0, 0.0, 0.0) #konokichur color set (RGB)
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
