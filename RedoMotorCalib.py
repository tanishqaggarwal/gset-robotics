from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()

psm.BAM1.setSpeed(70)
psm.BBM1.setSpeed(60)

sleep(5)

psm.BBM1.brake()
psm.BAM1.brake()
