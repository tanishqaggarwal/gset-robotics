from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()

psm.BAM1.setSpeed(50)
psm.BAM2.setSpeed(-50)

sleep(0.285)

psm.BAM1.brake()
psm.BAM2.brake()
