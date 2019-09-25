from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
from PIL import Image
import sys

cameraPosX = 0
cameraPosY = 0
cameraPosZ = 0

cameraMode = 0

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
    global cameraMode

    if cameraMode == 0:
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
    if cameraMode == 1:
        pass

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

def doTheMagic2 ():
    glutSwapBuffers ()

def pointCamera (eyeX, eyeY, eyeZ, lookPointX, lookPointY, lookPointZ):
    gluLookAt (eyeX, eyeY, eyeZ, lookPointX, lookPointY, lookPointZ, 0, -1, 0)

def idleFunction ():
    glutPostRedisplay ()

def Prepare (windowName, windowSizeX, windowSizeY, displayFunction, keyboardFunction, windowPositionX, windowPositionY):
    glutInit (sys.argv)
    glutInitDisplayMode (GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize (windowSizeX, windowSizeY)
    glutInitWindowPosition (windowPositionX, windowPositionY)

    glutCreateWindow (windowName)
    glutDisplayFunc (displayFunction)
    glutIdleFunc (idleFunction)
    glutReshapeFunc (reshapeFunction)
    glutKeyboardFunc (keyboardFunction)

def Launch ():
    init ()
    glutMainLoop ()



