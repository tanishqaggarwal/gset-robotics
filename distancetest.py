from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

def distance():
	return psm.BBS1.distanceUSEV3()

exit = False
while (not exit):

	print distance()

	if psm.isKeyPressed():
		psm.BBM1.brake()
		psm.BBM2.brake()
		psm.screen.clearScreen()
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		psm.led(1,0,0,0)    
		sleep(0.5)
		exit = True