from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()
hc = HiTechnicColorV2()
psm.BBS1.activateCustomSensorI2C()
blue = 2
red = 9
red2 = 8
counter = 0
last_time = datetime.now()
exit = False

botDiam = 17.5
wheelDiam = 6.5

target=90
translate=target*botDiam/(wheelDiam)

psm.BAM1.resetPos()
initialEncoderValue = psm.BAM1.pos()
while(psm.BAM1.pos()< translate+initialEncoderValue):
    psm.BAM1.setSpeed(50)
    psm.BAM2.setSpeed(-50)

psm.led(1, 255, 255, 255)
sleep(1)
psm.led(1,0,0,0)

psm.BAM1.brake()
psm.BAM2.brake()