# First, we enter the parent directory to import TRON library
import sys

sys.path.insert(1, '../')

# Then, we import our library
import TRON


# Simple drawing function to start with
def display():
    # A few lines to draw a square
    TRON.drawLine(1, 1, 1, 5, 1, 1)
    TRON.drawLine(5, 1, 1, 5, 1, 5)
    TRON.drawLine(5, 1, 5, 1, 1, 5)
    TRON.drawLine(1, 1, 5, 1, 1, 1)

    # A wire sphere with radius 1.5 and quality 50, positioned at (3, 1, 3)
    TRON.drawWireSphere(3, 1, 3, 1.5, 50)


# Create an app named "Example 1 - start an app", with window size 1280*720,
#	and 'display' function as drawing function
TRON.Prepare(b"Example 1 - start an app", 1280, 720, display)

# Look at point (3, 1, 3)
TRON.cameraLookAtX = 3
TRON.cameraLookAtY = 1
TRON.cameraLookAtZ = 3

# Disable movement
TRON.movementSpeed = 0.00
TRON.allowMovementSpeedChange = 0

# Start our app
TRON.Launch()
