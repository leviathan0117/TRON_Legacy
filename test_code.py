import TRON

def display ():
    TRON.doTheMagic()

    #TRON.pointCamera (TRON.cameraPosX, TRON.cameraPosY, TRON.cameraPosZ, TRON.cameraPosX, TRON.cameraPosY, TRON.cameraPosZ + 1)

    TRON.drawSphere (-1, 0, 3, 0.5, 10)
    TRON.drawSphere (1, 0, 3, 0.5, 100)
    TRON.drawSphere (-1, 0, 5, 0.5, 100)
    TRON.drawSphere (1, 0, 5, 0.5, 10)
    
    TRON.doTheMagic2()

    #print(str(TRON.cameraAngle1) + " " + str(TRON.cameraAngle2))

TRON.Prepare ("TRON example", 1280, 720, display, TRON.keyboardFunction, TRON.mouseButtonFunction, TRON.mouseMoveFunction, 100, 100)
#TRON.printMouseMoveEvent = 1
#TRON.printMouseButtonEvent = 1
TRON.Launch()