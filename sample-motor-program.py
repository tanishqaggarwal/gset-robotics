from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

psm.BAM1.setSpeedSync(75)

sleep(5)

psm.BAM1.float()