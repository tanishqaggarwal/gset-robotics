from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()



#exit variable will be used later to exit the program and return to PiStorms
exit = False
#so the initial condition is that it detects the black first
black = 700
white = 400
tolerance = (black-white)*.07
leftMotorSpeed = -75
rightMotorSpeed = -75


psm.BAM1.setSpeedSync(leftMotorSpeed)

def adjust(light):
	initialDifference = black-light
	psm.BAM1.setSpeed(75*-1)
	psm.BAM2.setSpeed(-1*initialDifference)
	sleep(.5)
	if (psm.BAS1.lightSensorNXT(True) <initialDifference) :
		#if the updated color is less (more white) than the initial difference
		psm.BAM1.setSpeed(-1*initialDifference)
		psm.BAM2.setSpeed(-75)

  

while(not exit):
	if (psm.BAS1.lightSensorNXT(True) < black -tolerance ):
		adjust(psm.BAS1.lightSensorNXT(True))
	elif (psm.BAS1.lightSensorNXT(True)>black):
		black = psm.BAS1.lightSensorNXT(True)
	psm.led(1,255,0,255) 
	sleep(0.1)
	if(psm.isKeyPressed() == True): # if the GO button is pressed
		psm.screen.clearScreen()
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		psm.led(1,0,0,0)
		sleep(0.5)
		exit = True



