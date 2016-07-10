from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()

psm.BAM2.setSpeed(-50)
psm.BBM1.setSpeed(-20)

sleep(5)

psm.BAM2.brake()
psm.BBM1.brake()
