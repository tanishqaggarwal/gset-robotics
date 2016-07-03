from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2

print "running program"

psm = PiStorms()
hc = HiTechnicColorV2()
psm.BBS1.activateCustomSensorI2C()
blue = 2
red = 9
red2 = 8

exit = False

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    color = hc.get_colornum()
    if(light <= 550):
        psm.BAM2.brake()
        psm.BAM1.setSpeed(-50)
    else:
        psm.BAM1.setSpeed(25)
        psm.BAM2.setSpeed(-50)
    if(color == red or color == red2):
        psm.BAM2.brake()
        psm.BAM1.brake()
    elif(color == blue):
        psm.screen.clearScreen()
        psm.screen.termPrintln("blue")
    if (psm.isKeyPressed()):
        psm.BAM1.brake()
        psm.BAM2.brake()
        exit = True
