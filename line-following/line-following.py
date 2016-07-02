from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

psm.BAM1.setSpeed(75)
psm.BBM1.setSpeed(75)

sleep(5)

psm.BAM1.float()
psm.BBM1.float()