from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

psm = PiStorms()

psm.BAM1.setSpeedSync(50)
sleep(10)
psm.BAM1.brake()
psm.BAM2.brake()
