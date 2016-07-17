from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

DISTANCE_THRESHOLD = 90

WHITE_THRESHOLD = ""

ALTERNATOR = 1 # Used if I fucked up the motor orientation and -1 is actually how we move forward
INV_ALTERNATOR = 0 - ALTERNATOR

sleep(5)

def distance():
	return psm.BAS1.distanceUSEV3()

def seeing_other_robot():
	return distance() < DISTANCE_THRESHOLD

def near_edge():
	return psm.BAS2.lightSensorNXT(True) > WHITE_THRESHOLD

def gtfo():
	def turn_180():
		psm.BAM1.setSpeed(ALTERNATOR * 100)
		psm.BAM2.setSpeed(INV_ALTERNATOR * 100)
		sleep(0.6)
		psm.BAM1.brake()
		psm.BAM2.brake()
		sleep(0.01)

	psm.BAM1.setSpeed(INV_ALTERNATOR * 100)
	psm.BAM2.setSpeed(INV_ALTERNATOR * 100)
	sleep(0.2)
	#turn_180()

def find_other_robot():
	psm.BAM1.setSpeed(ALTERNATOR * 100)
	psm.BAM2.setSpeed(INV_ALTENRATOR * 100)
	if seeing_other_robot():
		psm.BAM1.brake()
		psm.BAM2.brake()
		sleep(0.01)

def charge():
	psm.BAM1.setSpeed(ALTERNATOR * 100)
	psm.BAM2.setSpeed(ALTERNATOR * 100)

exit = False
while (not exit):

	if near_edge():
		gtfo()

	if seeing_other_robot():
		charge()
	else:
		find_other_robot()

	if psm.isKeyPressed():
		psm.BAM1.brake()
		psm.BAM2.brake()
		psm.screen.clearScreen()
	    psm.screen.termPrintln("")
	    psm.screen.termPrintln("Exiting to menu")
	    psm.led(1,0,0,0)    
	    sleep(0.5)
	    exit = True