from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()


exit = False

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    
    if (light <= 550):
    	psm.BAM2.brake()
    	psm.BAM1.setSpeed(-50)
    else:
    	psm.BAM1.brake()
    	psm.BAM2.setSpeed(-75)

    if (psm.isKeyPressed()):
    	psm.BAM1.brake()
    	psm.BAM2.brake()
        exit = True