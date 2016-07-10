from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()

def brake():
    psm.BAM1.brake()
    psm.BBM1.brake()

def ninetydegrees(direction):
    if direction == "right":
        s = 1
    else:
        s = -1

    psm.BAM1.setSpeed(s * 100)
    psm.BBM1.setSpeed(s * -100)
    sleep(0.285)
    brake()

ninetydegrees("left")
sleep(1)
ninetydegrees("left")
sleep(1)
ninetydegrees("left")
sleep(1)
ninetydegrees("left")
