from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()

psm.BAM1.setSpeedSync(20)
sleep(5)
psm.BAM1.brake()