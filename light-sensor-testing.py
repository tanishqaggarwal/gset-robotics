 from PiStorms import PiStorms
 from time import sleep
 print "running program"
 psm = PiStorms()
 
 exit = False
 
 while(not exit):
     light = psm.BAS1.lightSensorNXT(True)
     psm.screen.clearScreen()
     psm.screen.termPrintln(str(light))
 
     if (psm.isKeyPressed() == True):
         exit = True 
