from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()


exit = False

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    
    if (light <= 550):
    	psm.BAM2.setSpeed(12)
    	psm.BAM1.setSpeed(-25)
    else:
    	psm.BAM1.brake()
    	psm.BAM1.setSpeed(12)
    	psm.BAM2.setSpeed(-25)

    if (psm.isKeyPressed()):
    	psm.BAM1.brake()
    	psm.BAM2.brake()
        exit = True