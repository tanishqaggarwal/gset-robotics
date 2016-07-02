from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

exit = True

WHITE = 600
BLACK = 800
TOLERANCE = 20

psm.BAM1.setSpeedSync()

previous_difference = 0
direction = "LEFT" #Or "RIGHT"
while (not exit):
	light = psm.BAS1.lightSensorNXT(True)
	current_difference = abs(light - BLACK)

	if current_difference > TOLERANCE:
		if previous_difference < current_difference:
			


	previous_difference = current_difference



# psm.BAM1.setSpeed(75)
# psm.BBM1.setSpeed(75)

# sleep(5)

# psm.BAM1.float()
# psm.BBM1.float()