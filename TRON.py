from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
from PIL import Image
import sys
import math

######################################## CAMERA:
cameraMode = 0

# Camera position in (X, Y, Z)
cameraPosX = 0
cameraPosY = 0
cameraPosZ = 0

# Point at which the camera looks in (X, Y, Z)
cameraLookAtX = 0
cameraLookAtY = 0
cameraLookAtZ = 0

# Regulates how sensitive camera movement would be to mouse movement. Original value = 0.005
cameraSensitivity = 0.005

#################### Parameters for CONST_CameraRevolve (0):
cameraAngle1 = 0
cameraAngle2 = 0

#################### Parameters for CONST_CameraFly (1):


######################################## Movement:
movementMode = 0
movementSpeed = 0.1

# Allows / prohibits changing movement speed
allowMovementSpeedChange = 1

######################################## DRAWING:
colorR = 1
colorG = 1
colorB = 1

######################################## LOG parameters:
printMouseButtonEvent = 0
printMouseMoveEvent = 0

######################################## CONSTANTS:
#!!!!! CONSTANTS WORK ONLY WITHIN DEFAULT FUNCTIONS !!!!!

# Makes camera revolve around a certain point
CONST_CameraRevolve = 0 

# Makes camera look around FROM a specific point
CONST_CameraLookAroung = 1

# Makes camera move in a plane - WASD keys are for changin plane coordinates, C or SPACE for rising/lowing down the plane
CONST_MoveField = 0

def init ():
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glClearDepth (1.0) 
    glDepthFunc (GL_LEQUAL)
    glEnable (GL_DEPTH_TEST)
    glEnable (GL_TEXTURE_2D)
    glHint (GL_POLYGON_SMOOTH_HINT,         GL_NICEST)
    glHint (GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)

def loadTexture (fileName):
    image  = Image.open (fileName)
    width  = image.size [0]
    height = image.size [1]
    image  = image.tobytes ("raw", "RGBX", 0, -1)
    texture = glGenTextures (1)
    
    glBindTexture (GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
    glPixelStorei (GL_UNPACK_ALIGNMENT,1)
    glTexParameterf (GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf (GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri (GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    glTexParameteri (GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR_MIPMAP_LINEAR)
    gluBuild2DMipmaps (GL_TEXTURE_2D, 3, width, height, GL_RGBA, GL_UNSIGNED_BYTE, image)
    
    return texture

# TODO: find out why only one keyboard button can work at a time
def keyboardFunction ( *args ):
    if args [0] == b'\x1b':
        sys.exit ()

    global cameraPosX, cameraPosY, cameraPosZ
    global cameraLookAtX, cameraLookAtY, cameraLookAtZ
    global cameraMode, movementMode
    global movementSpeed, allowMovementSpeedChange

    # TODO: prove this should work theoretically:
    if movementMode == 0:
        if args [0] == b'w':
            cameraLookAtZ -= movementSpeed * math.cos(cameraAngle1 - math.pi / 2)
            cameraLookAtX -= movementSpeed * math.sin(cameraAngle1 - math.pi / 2)
        if args [0] == b's':
            cameraLookAtZ += movementSpeed * math.cos(cameraAngle1 - math.pi / 2)
            cameraLookAtX += movementSpeed * math.sin(cameraAngle1 - math.pi / 2)
        if args [0] == b'd':
            cameraLookAtZ -= movementSpeed * math.cos(cameraAngle1)
            cameraLookAtX -= movementSpeed * math.sin(cameraAngle1)
        if args [0] == b'a':
            cameraLookAtZ += movementSpeed * math.cos(cameraAngle1)
            cameraLookAtX += movementSpeed * math.sin(cameraAngle1)
        if args [0] == b'c':
            cameraLookAtY += movementSpeed
        if args [0] == b' ':
            cameraLookAtY -= movementSpeed
        if args [0] == b'e' and allowMovementSpeedChange:
            movementSpeed += 0.01
        if args [0] == b'q' and allowMovementSpeedChange:
            movementSpeed -= 0.01
            if movementSpeed < 0:
                movementSpeed = 0


    if cameraMode == 1:
        if args [0] == b'w':
            cameraPosZ += 0.1
        if args [0] == b's':
            cameraPosZ -= 0.1
        if args [0] == b'd':
            cameraPosX += 0.1
        if args [0] == b'a':
            cameraPosX -= 0.1
        if args [0] == b'c':
            cameraPosY += 0.1
        if args [0] == b' ':
            cameraPosY -= 0.1
        cameraLookAtX = cameraPosX
        cameraLookAtY = cameraPosY
        cameraLookAtZ = cameraPosZ + 1

def reshapeFunction (width, height):
    glViewport     (0, 0, width, height)
    glMatrixMode   (GL_PROJECTION)
    glLoadIdentity ()
    gluPerspective (60.0, float(width)/float (height), 1.0, 60.0)
    glMatrixMode   (GL_MODELVIEW)
    glLoadIdentity ()

def doTheMagic ():
    glClear        (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode   (GL_MODELVIEW)
    glLoadIdentity ()

    global cameraAngle1, cameraAngle2
    global cameraPosX, cameraPosY, cameraPosZ
    global cameraLookAtX, cameraLookAtY, cameraLookAtZ

    lx = -math.cos(cameraAngle1) * math.cos(cameraAngle2)
    ly = math.sin(cameraAngle2)
    lz = math.sin(cameraAngle1) * math.cos(cameraAngle2)
    cameraPosX = cameraLookAtX + lx * 4
    cameraPosY = cameraLookAtY + ly * 4
    cameraPosZ = cameraLookAtZ + lz * 4

    gluLookAt (cameraPosX, cameraPosY, cameraPosZ,
                cameraLookAtX, cameraLookAtY, cameraLookAtZ,
                0, -1, 0)

def doTheMagic2 ():
    glutSwapBuffers ()

def pointCamera (eyeX, eyeY, eyeZ, lookPointX, lookPointY, lookPointZ):
    glClear        (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode   (GL_MODELVIEW)
    glLoadIdentity ()
    gluLookAt (eyeX, eyeY, eyeZ, lookPointX, lookPointY, lookPointZ, 0, -1, 0)

def idleFunction ():
    glutPostRedisplay ()


mouseXPrev = -12345789
mouseYPrev = -12345789

#Default function for mouse button events:
def mouseButtonFunction (buttonID, buttonState, mouseX, mouseY):
    if printMouseButtonEvent:
        if buttonID == GLUT_LEFT_BUTTON:
            if buttonState == GLUT_DOWN:
                print("Left button down", end="")
            else:
                print("Left button up", end="")
        else:
            if buttonState == GLUT_DOWN:
                print("Right button down", end="")
            else:
                print("Right button up", end="")
        print(" || Mouse position: (" + str(mouseX) + ", " + str(mouseY) + ")")
    global mouseXPrev, mouseYPrev
    mouseXPrev = mouseX
    mouseYPrev = mouseY

#Default function for mouse movements (if any button pressed):
def mouseMoveFunction (mouseX, mouseY):
    global mouseXPrev, mouseYPrev
    global cameraAngle1, cameraAngle2

    deltaX = mouseX - mouseXPrev
    deltaY = mouseY - mouseYPrev

    cameraAngle1 += deltaX * cameraSensitivity
    cameraAngle2 -= deltaY * cameraSensitivity
    #the 0.01 - is a bug fixer which doesn't allow for Pi/2 or close to Pi/2 angles (as it results in strange behavior)
    #TODO: fix this problem somehow
    if cameraAngle2 >= math.pi / 2 - 0.01: 
        cameraAngle2 = math.pi / 2 - 0.01
    elif cameraAngle2 <= -math.pi / 2 + 0.01:
        cameraAngle2 = -math.pi / 2 + 0.01
    mouseXPrev = mouseX
    mouseYPrev = mouseY

    if printMouseMoveEvent:
        print("Mouse moved || Mouse position: (" + str(mouseX) + ", " + str(mouseY) + ")")

def Prepare (windowName, windowSizeX, windowSizeY, displayFunction, keyboardFunction, mouseButtonFunction, mouseMoveFunction, windowPositionX, windowPositionY):
    glutInit (sys.argv)
    glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize (windowSizeX, windowSizeY)
    glutInitWindowPosition (windowPositionX, windowPositionY)

    glutCreateWindow (windowName)
    glutDisplayFunc (displayFunction)
    glutIdleFunc (idleFunction)
    glutReshapeFunc (reshapeFunction)
    glutKeyboardFunc (keyboardFunction)
    glutMouseFunc(mouseButtonFunction)
    glutMotionFunc(mouseMoveFunction)

def Launch ():
    init ()
    glutMainLoop ()


################################################## Drawing functions:

def setColorRGB256 (colorRIn, colorGIn, colorBIn):
    global colorR, colorG, colorB

    colorR = colorRIn / 255
    colorG = colorGIn / 255
    colorB = colorBIn / 255

def setColorRGB (colorRIn, colorGIn, colorBIn):
    if colorRIn > 1 or colorGIn > 1 or colorBIn > 1:
        print ("WRONG COLOR FUNCTION USED (0..1 instead of 0..255)")
    else:
        global colorR, colorG, colorB

        colorR = colorRIn
        colorG = colorGIn
        colorB = colorBIn

def drawSphere (xPosition, yPosition, zPosition, radius, quality):
    glColor3f(colorR, colorG, colorB)

    glPushMatrix()

    glTranslatef (xPosition, yPosition, zPosition)
    glutSolidSphere(radius, quality, quality)

    glPopMatrix()

def drawLine (xPosition1, yPosition1, zPosition1, xPosition2, yPosition2, zPosition2):
    glColor3f(colorR, colorG, colorB)

    glBegin(GL_LINES);
    glVertex3f(xPosition1, yPosition1, zPosition1);
    glVertex3f(xPosition2, yPosition2, zPosition2);
    glEnd();    
