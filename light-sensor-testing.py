from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()
 
exit = False
 
while(not exit):
    light = psm.BAS2.lightSensorNXT(True)
    print light

    if (psm.isKeyPressed() == True):
        exit = True 
