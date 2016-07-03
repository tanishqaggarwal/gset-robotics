from PiStorms import PiStorms
from time import sleep
print "running program"
psm=PiStorms()



#exit variable will be used later to exit the program and return to PiStorms
exit=False
black=700
white=400
initspeed=-50

average=(black+white)/2
RANGE=(black-average)*1.1
MAX=75-abs(initspeed)

while(not exit):
	proportions=MAX*(psm.BAS1.lightSensorNXT(True)-average)/RANGE
	psm.BAM1.setSpeed(initspeed-proportions)
	psm.BAM2.setSpeed(initspeed+proportions)

	psm.led(1,255,0,255) 
	sleep(0.01)

	if(psm.isKeyPressed()): # if the GO button is pressed
		psm.screen.clearScreen()
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		psm.led(1,0,0,0)

		psm.BAM1.brake()
		psm.BAM2.brake()
		psm.BBM1.brake()
		psm.BBM2.brake()
		sleep(0.5)
		
		exit = True
		break