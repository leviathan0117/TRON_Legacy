# First, we enter the parent directory to import TRON library
import sys

sys.path.insert(1, '../')

# Then, we import our library and other needed libraries
import TRON
import random

# Size of sphere cube
sizeCube = 5
# Create a FPS measurer, that will print the result every two seconds
frameRate = TRON.FPS(2)
# Create an array to store sphere colors and fill it randomly
colors = [[[[random.randint(0, 256) for color in range(3)] for x in range(sizeCube * 2 + 1)] for y in range(sizeCube * 2 + 1)] for z in range(sizeCube * 2 + 1)]


# Simple drawing function to start with
def display():
    global sizeCube

    for x in range(-sizeCube, sizeCube + 1):
        for y in range(-sizeCube, sizeCube + 1):
            for z in range(-sizeCube, sizeCube + 1):
                # Set a color associated with a sphere
                TRON.setColorRGB256(colors[x + sizeCube][y + sizeCube][z + sizeCube][0],
                                    colors[x + sizeCube][y + sizeCube][z + sizeCube][1],
                                    colors[x + sizeCube][y + sizeCube][z + sizeCube][2])
                # A sphere with radius 0.3 and quality 50, positioned at (x, y, z)
                TRON.drawSphere(x, y, z, 0.3, 10)

    # Print current FPS to console
    frameRate.updateAndPrint()


# Create an app named "Example 2 - FPS measurement", with window size 1280*720,
#	and 'display' function as drawing function
TRON.Prepare(b"Example 2 - FPS measurement", 1280, 720, display)

# Start our app
TRON.Launch()
