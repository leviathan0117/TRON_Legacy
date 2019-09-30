#First, we import our library.
import TRON

#Simple drawing function to start with
def display():
	#A few lines to draw a square
	TRON.drawLine(1, 1, 1, 2, 1, 1)
	TRON.drawLine(2, 1, 1, 2, 1, 2)
	TRON.drawLine(2, 1, 2, 1, 1, 2)
	TRON.drawLine(1, 1, 2, 1, 1, 1)

	#A sphere with radius 0.3 and quality 10
	TRON.drawSphere(1.5, 1, 1.5, 0.3, 10)

#Create an app named "Example 1 - start an app", with window size 1280*720,
#	and 'display' function as drawing function
TRON.Prepare ("Example 1 - start an app", 1280, 720, display)

#Look at point 1.5, 1, 1.5
TRON.cameraLookAtX = 1.5
TRON.cameraLookAtY = 1
TRON.cameraLookAtZ = 1.5

#Start our app
TRON.Launch()