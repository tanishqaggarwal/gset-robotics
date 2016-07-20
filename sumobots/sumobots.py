from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

DISTANCE_THRESHOLD = 700

WHITE_THRESHOLD = 400
BLACK_THRESHOLD = 700
WHITE = [12,13,14]

ALTERNATOR = 1 # Used if I fucked up the motor orientation and -1 is actually how we move forward
INV_ALTERNATOR = 0 - ALTERNATOR

sleep(5)

def distance():
	return psm.BBS1.distanceUSEV3()

def seeing_other_robot():
	return distance() < DISTANCE_THRESHOLD

def near_edge():
	return psm.BAS2.lightSensorNXT(True) > WHITE_THRESHOLD and psm.BAS2.lightSensorNXT(True) < BLACK_THRESHOLD or psm.BAS1.colorSensorNXT() in WHITE

def gtfo():
	def turn_180():
		psm.BBM1.setSpeed(ALTERNATOR * 100)
		psm.BBM2.setSpeed(INV_ALTERNATOR * 100)
		sleep(0.6)
		psm.BBM1.brake()
		psm.BBM2.brake()
		sleep(0.01)

	psm.BBM1.setSpeed(INV_ALTERNATOR * 100)
	psm.BBM2.setSpeed(INV_ALTERNATOR * 100)
	sleep(0.2)
	#turn_180()

def find_other_robot():
	psm.BBM1.setSpeed(ALTERNATOR * 100)
	psm.BBM2.setSpeed(INV_ALTERNATOR * 100)
	if seeing_other_robot():
		psm.BBM1.brake()
		psm.BBM2.brake()
		sleep(0.01)

def charge():
	psm.BBM1.setSpeed(ALTERNATOR * 100)
	psm.BBM2.setSpeed(ALTERNATOR * 100)

exit = False
while (not exit):

	if near_edge():
		gtfo()

	if seeing_other_robot():
		charge()
	else:
		find_other_robot()

	if psm.isKeyPressed():
		psm.BBM1.brake()
		psm.BBM2.brake()
		psm.screen.clearScreen()
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		psm.led(1,0,0,0)    
		sleep(0.5)
		exit = True
