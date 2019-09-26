import TRON
import math
def display ():
    sz = 40
    for x in range (sz):
        for z in range (sz):
            blue = (x * z) / (sz**2) * 4
            if blue > 1:
                blue = 1
            TRON.setColorRGB(x / sz, z / sz, blue)
            TRON.drawSphere(x-sz/2, 0, z-sz/2, 1, 20)  
TRON.Prepare ("TRON example", 1280, 720, display, TRON.keyboardFunction, TRON.mouseButtonFunction, TRON.mouseMoveFunction, 100, 100)
TRON.cameraLookAtY = -30
TRON.cameraAngle2 = -math.pi/2+0.01
TRON.Launch()