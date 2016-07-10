from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()

psm.BBM1.setSpeed(50)
psm.BBM2.setSpeed(-50)

sleep(0.2855)

psm.BBM1.brake()
psm.BBM2.brake()
