from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from threading import Thread

print "running program"
psm = PiStorms()

#exit variable will be used later to exit the program and return to PiStorms
exit = False

def linefollow():
    while(not exit):
        light = psm.BAS1.lightSensorNXT(True)
        
        if (light <= 550):
            psm.BAM2.brake()
            psm.BAM1.setSpeed(-100)
        else:
            psm.BAM1.setSpeed(50)
            psm.BAM2.setSpeed(-100)

        if (psm.isKeyPressed()):
            psm.BAM1.brake()
            psm.BAM2.brake()
            exit = True
    psm.BAM1.brake()
    psm.BAM2.brake()
    psm.BBM1.brake()
    psm.BBM2.brake()

def findvicts():
    while(not exit):
        color=hc.get_colornum()
        if color==9:  #Red
            psm.led(1,255,0,0)
            sleep(3)
            psm.led(1,0,0,0)
            sleep(2)  #need to sleep long enough to not double count   
        sleep(0.1)
        psm.led(1,0,0,0)  #Should not be needed but is safer


hc=HiTechnicColorV2()
psm.BBS1.activateCustomSensorI2C()


lf = Thread(target=linefollow)
lf.start()
fv = Thread(target=findvicts)
fv.start()

#Main Loop
while(not exit):
  sleep(0.05)
  
  if(psm.isKeyPressed() == True): # if the GO button is pressed
    psm.screen.clearScreen()
    psm.screen.termPrintln("")
    psm.screen.termPrintln("Exiting to menu")
    psm.led(1,0,0,0)
    psm.BAM1.brake()
    psm.BAM2.brake()
    psm.BBM1.brake()
    psm.BBM2.brake()    
    sleep(0.5)
    exit = True