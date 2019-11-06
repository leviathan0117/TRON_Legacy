import TRON
import time

start_time = time.time()
interval = 2 # displays the frame rate every 2 seconds
counter = 0

angleSpeed = 0

def display ():
    sz = 10
    for x in range (sz):
        for z in range (sz):
            for y in range(sz):
                if x == sz - 1 or y == sz - 1 or z == sz - 1 or x * y * z == 0:
                    TRON.setColorRGB(x / sz, z / sz, 1 - y / sz)
                    #TRON.drawSphere(x-sz/2, y-sz/2, z-sz/2, 0.1, 10)
                    TRON.drawBox(x - sz / 2, y - sz / 2, z - sz / 2, 1)

    TRON.cameraAngle1 -= angleSpeed

    global counter, start_time, interval
    counter += 1
    if (time.time() - start_time) > interval:
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()

def aditionalKeyboardHandle():
    global angleSpeed
    if TRON.keyState['e']:
        angleSpeed = 0.02
    if TRON.keyState['q']:
        angleSpeed = -0.02
    if TRON.keyState['r']:
        angleSpeed = 0

TRON.Prepare (b"TRON example", 1280, 720, display, aditionalKeyboardHandle, None, None, (1920 - 1280) / 2, (1080 - 720) / 2)

TRON.cameraSensitivity = 0.002
TRON.cameraDistanceToObject = 20
TRON.movementSpeed = 0.1

TRON.Launch()