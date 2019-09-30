import TRON
import math
import time

start_time = time.time()
interval = 1 # displays the frame rate every 1 secon
counter = 0

def display ():
    sz = 40
    for x in range (sz):
        for z in range (sz):
            blue = (x * z) / (sz**2) * 4
            if blue > 1:
                blue = 1
            
            TRON.setColorRGB(x / sz, z / sz, blue)
            TRON.drawSphere(x-sz/2, 0, z-sz/2, 0.3, 13)

    global counter, start_time, interval
    counter += 1
    if (time.time() - start_time) > interval:
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time() 

def aditionalKeyboardHandle():
    if TRON.keyState['p']:
        print("Hello world!")

TRON.Prepare ("TRON example", 1280, 720, display, aditionalKeyboardHandle, None, None, 100, 100)

TRON.cameraLookAtY = -30
TRON.cameraAngle2 = -math.pi/2+0.01

TRON.Launch()