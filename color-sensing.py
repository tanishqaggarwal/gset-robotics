from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime
import os

exit = False

psm=PiStorms()
hc=HiTechnicColorV2()
psm.BAS1.activateCustomSensorI2C()

while(not exit):
	color=hc.get_colornum()
	print color
	if(psm.isKeyPressed() == True): # if the GO button is pressed
		psm.screen.clearScreen()
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		sleep(0.5)
		exit = True