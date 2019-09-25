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
cameraLookAtZ = 4

#################### Parameters for CONST_CameraRevolve (0):
cameraAngle1 = 0
cameraAngle2 = 0

#################### Parameters for CONST_CameraFly (1):


######################################## LOG parameters:
printMouseButtonEvent = 0
printMouseMoveEvent = 0

######################################## CONSTANTS:

# If setted to cameraMode and used with default mouse functions - will make camera revolve around a certain point
CONST_CameraRevolve = 0 

# If setted to cameraMode and used with default mouse functions - will make camera 'fly' through 3D space
CONST_CameraFly = 1

def drawSphere (xPosition, yPosition, zPosition, radius, quality):
    glPushMatrix()
    glTranslatef   (xPosition, yPosition, zPosition)
    glutSolidSphere(radius, quality, quality)
    glPopMatrix()

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

def keyboardFunction ( *args ):
    if args [0] == b'\x1b':
        sys.exit ()

    global cameraPosX, cameraPosY, cameraPosZ
    global cameraLookAtX, cameraLookAtY, cameraLookAtZ
    global cameraMode

    if cameraMode == 0:
        pass

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
    cameraAngle1 += deltaX * 0.005
    cameraAngle2 -= deltaY * 0.005
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



