import TRON
import math
from TRON_import import *
import time

start_time = time.time()
interval = 2 # displays the frame rate every 2 seconds
counter = 0

angleSpeed = 0

def display ():
    sz = 10
    TRON.cameraAngle1 -= angleSpeed
    for x in range (sz):
        for z in range (sz):
            for y in range(sz):
                TRON.setColorRGB(x / sz, z / sz, 1 - y / sz)
                TRON.drawSphere(x-sz/2, y-sz/2, z-sz/2, 0.3, 10)

    global counter, start_time, interval
    counter += 1
    if (time.time() - start_time) > interval:
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()

def aditionalKeyboardHandle():
    global angleSpeed
    if TRON.keyState['e']:
        angleSpeed = 0.01
    if TRON.keyState['q']:
        angleSpeed = -0.01
    if TRON.keyState['r']:
        angleSpeed = 0

TRON.Prepare (b"TRON example", 1280, 720, display, aditionalKeyboardHandle, None, None, None, (1920 - 1280) / 2, (1080 - 720) / 2)

TRON.cameraSensitivity = 0.002
TRON.cameraDistanceToObject = 20
TRON.movementSpeed = 0.1

#TRON.cameraMode = TRON.CONST_CameraLookAround
#TRON.movementMode = TRON.CONST_MoveAround

TRON.Launch()