from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def FindZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = None
    if (abs(dx) > abs(dy)):
        if(dx>0 and dy >=0):
            zone = 0
        elif(dx>0 and dy<=0):
            zone = 7
        elif(dx<0 and dy>=0):
            zone = 3
        elif(dx<0 and dy<=0):
            zone = 4

    else:
        if(dy>0 and dx>=0):
            zone = 1
        elif(dy>0 and dx<=0):
            zone = 2
        elif(dy<0 and dx<=0):
            zone = 5
        elif(dy<0 and dx>=0):
            zone = 6

        return zone

def ConvertToZone0(x, y, zone):
    if(zone == 0):
        x, y = x, y
    elif(zone == 1):
        x, y = y, x
    elif (zone == 2):
        x, y = y, -x
    elif (zone == 3):
        x, y = -x, y
    elif (zone == 4):
        x, y = -x, -y
    elif (zone == 5):
        x, y = -y, -x
    elif (zone == 6):
        x, y = -y, x
    elif (zone == 7):
        x, y = x, -y

    return x, y

def MidPointLine(x1, y1, x2, y2):
    zone = FindZone(x1, y1, x2, y2)
    x1, y1 = ConvertToZone0(x1, y1, zone)
    x2, y2 = ConvertToZone0(x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    D_init = 2*dy - dx
    D_NE = 2*(dy - dx)
    D_E = 2*dy
    x = x1
    y = y1
    while (x <= x2):
        x_new, y_new = ConvertToOriginalZone(x, y, zone)
        draw_points(x_new, y_new)
        x += 1

        if (D_init<0):
            x_new, y_new = ConvertToOriginalZone(x, y, zone)
            draw_points(x_new, y_new)
            D_init = D_init + D_E
        else:
            x_new, y_new = ConvertToOriginalZone(x, y, zone)
            draw_points(x_new, y_new)
            D_init = D_init + D_NE
            y += 1

def ConvertToOriginalZone(x, y, zone):

    if (zone == 0):
        x, y = x, y
    elif (zone == 1):
        x, y = y, x
    elif (zone == 2):
        x, y = -y, x
    elif (zone == 3):
        x, y = -x, y
    elif (zone == 4):
        x, y = -x, -y
    elif (zone == 5):
        x, y = -y, -x
    elif (zone == 6):
        x, y = y, -x
    elif (zone == 7):
        x, y = x, -y

    return x, y

ID = input("ID: ")
n = []
for i in ID:
    n.append(i)
def Last_2_digits():

    if n[6]=="0":
        MidPointLine(100, 100, 240, 100)  # Bottom line
        MidPointLine(100, 400, 240, 400)  # Top line
        MidPointLine(100, 100, 100, 400)  # Left Line
        MidPointLine(240, 100, 240, 400)  # Right Line

    if n[6]=="1":
        MidPointLine(100, 325, 170, 400)  # Up line
        MidPointLine(170, 100, 170, 400)  # Straight Line
        MidPointLine(100, 100, 240, 100)  # Bottom line

    if n[6]=="2":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(240, 250, 240, 400)  # Up right
        MidPointLine(100, 250, 240, 250)  # Middle line
        MidPointLine(100, 100, 100, 250)  # Bottom left
        MidPointLine(100, 100, 240, 100)  # Bottom line
    if n[6]=="3":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(240, 100, 240, 400)  # Right line
        MidPointLine(100, 250, 240, 250)  # Middle line
        MidPointLine(100, 100, 240, 100)  # Bottom line

    if n[6]=="4":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(100, 250, 100, 400)  # Left line
        MidPointLine(240, 100, 240, 400)  # Right line
        MidPointLine(100, 250, 240, 250)  # Middle line
    if n[6]=="5":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(100, 250, 240, 250)  # Middle line
        MidPointLine(100, 100, 240, 100)  # Bottom line
        MidPointLine(100, 250, 100, 400)  # Left line
        MidPointLine(240, 100, 240, 250)  # Right line
    if n[6]=="6":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(100, 250, 240, 250)  # Middle line
        MidPointLine(100, 100, 240, 100)  # Bottom line
        MidPointLine(240, 100, 240, 250)  # Right line
        MidPointLine(100, 100, 100, 400)  # Left line

    if n[6]=="7":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(140, 100, 240, 400)  # Right line

    if n[6]=="8":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(100, 250, 240, 250)  # Middle line
        MidPointLine(100, 100, 240, 100)  # Bottom line
        MidPointLine(100, 100, 100, 400)  # Left line
        MidPointLine(240, 100, 240, 400)  # Right line

    if n[6]=="9":
        MidPointLine(100, 400, 240, 400)  # Up line
        MidPointLine(100, 250, 240, 250)  # Middle line
        MidPointLine(100, 100, 240, 100)  # Bottom line
        MidPointLine(240, 100, 240, 400)  # Right line
        MidPointLine(100, 250, 100, 400)  # Left line

    if n[7] == "0":
        MidPointLine(260, 100, 400, 100)  # Bottom line
        MidPointLine(260, 400, 400, 400)  # Top line
        MidPointLine(260, 100, 260, 400)  # Left Line
        MidPointLine(400, 100, 400, 400)  # Right Line

    if n[7] == "1":
        MidPointLine(260, 332, 330, 400)  # Up line
        MidPointLine(330, 100, 330, 400)  # Straight Line
        MidPointLine(260, 100, 400, 100)  # Bottom line

    if n[7] == "2":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(400, 250, 400, 400)  # Up right
        MidPointLine(260, 250, 400, 250)  # Middle line
        MidPointLine(260, 100, 260, 250)  # Bottom left
        MidPointLine(260, 100, 400, 100)  # Bottom line
    if n[7] == "3":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(400, 100, 400, 400)  # Right line
        MidPointLine(260, 250, 400, 250)  # Middle line
        MidPointLine(260, 100, 400, 100)  # Bottom line

    if n[7] == "4":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(260, 250, 260, 400)  # Left line
        MidPointLine(400, 100, 400, 400)  # Right line
        MidPointLine(260, 250, 400, 250)  # Middle line
    if n[7] == "5":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(260, 250, 400, 250)  # Middle line
        MidPointLine(260, 100, 400, 100)  # Bottom line
        MidPointLine(260, 250, 260, 400)  # Left line
        MidPointLine(400, 100, 400, 250)  # Right line
    if n[7] == "6":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(260, 250, 400, 250)  # Middle line
        MidPointLine(260, 100, 400, 100)  # Bottom line
        MidPointLine(400, 100, 400, 250)  # Right line
        MidPointLine(260, 100, 260, 400)  # Left line

    if n[7] == "7":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(300, 100, 400, 400)  # Right line

    if n[7] == "8":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(260, 250, 400, 250)  # Middle line
        MidPointLine(260, 100, 400, 100)  # Bottom line
        MidPointLine(260, 100, 260, 400)  # Left line
        MidPointLine(400, 100, 400, 400)  # Right line

    if n[7] == "9":
        MidPointLine(260, 400, 400, 400)  # Up line
        MidPointLine(260, 250, 400, 250)  # Middle line
        MidPointLine(260, 100, 400, 100)  # Bottom line
        MidPointLine(400, 100, 400, 400)  # Right line
        MidPointLine(260, 250, 260, 400)  # Left line


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
    glColor3f(1.0, 0.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    Last_2_digits()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()
