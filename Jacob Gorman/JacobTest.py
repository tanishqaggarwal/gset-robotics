from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

blue = 2
red = 8

exit = False

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    color = psm.BBS1.colorSensorNXT(True)
    if(light <= 550):
        psm.BAM2.brake()
        psm.BAM1.setSpeed(-50)
    else:
        psm.BAM1.setSpeed(25)
        psm.BAM2.setSpeed(-50)
    if(color == red):
        psm.BAM2.brake()
        psm.BAM1.brake()
    elif(color == blue:
        psm.screen.termprintln("blue")
    if (psm.isKeyPressed()):
        psm.BAM1.brake()
        psm.BAM2.brake()
        exit = True
