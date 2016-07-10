from PiStorms import PiStorms
from time import sleep
from HiTechnicColorV2 import HiTechnicColorV2
from datetime import datetime

print "running program"

psm = PiStorms()
hc = HiTechnicColorV2()
psm.BBS1.activateCustomSensorI2C()
blue = 2
red = 9
red2 = 8
green = 4
purple = 12

counter = 0
last_time = datetime.now()
exit = False

def ninetydegrees(s) :
    psm.BBM1.setSpeed(s * 50)
    psm.BBM2.setSpeed(s * -50)
    sleep(0.285)
    psm.BBM2.brake()
    psm.BBM1.brake()

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    color = hc.get_colornum()
    if(light <= 550):
        psm.BBM2.brake()
        psm.BBM1.setSpeed(-25)
    else:
        psm.BBM1.setSpeed(12.5)
        psm.BBM2.setSpeed(-5)
    if(color == red or color == red2):
        psm.BBM2.brake()
        psm.BBM1.brake()
        psm.screen.clearScreen()
        psm.screen.termPrintln(str(counter))
        exit = True
    elif(color == blue):
        if((datetime.now() - last_time).seconds > 0):
            counter += 1
            last_time = datetime.now()
            psm.screen.clearScreen()
            psm.screen.termPrintln("I'm functioning Properly")
    if (psm.isKeyPressed()):
        psm.BBM1.brake()
        psm.BBM2.brake()
        exit = True

psm.led(1, 255, 255, 255)
sleep(1)
psm.led(1,0,0,0)

psm.BBM1.setSpeed(-50)
psm.BBM2.setSpeed(-50)
sleep(2.5)
"""psm.BBM1.setSpeedSync(50)
sleep(0.2)
ninetydegrees(1)

greenfound = False

t = datetime.now()
done = False
while(not done and (datetime.now() - t).seconds < 15):
    psm.BBM1.setSpeedSync(-50)
    color = hc.get_colornum()
    if color == green:
        sleep(0.5)
        psm.BBM1.brake()
        psm.BBM2.brake()
        done = True
        greenfound = True
        break

if not greenfound:
    t = datetime.now()
    done = False
    while(not done and (datetime.now()-t).seconds < 20):
        psm.BBM1.setSpeedSync(-50)
        color = hc.get_colornum()
        if color == green:
            sleep(0.5)
            psm.BBM1.brake()
            psm.BBM2.brake()
            done = True
            greenfound = True
            break

    if not greenfound:
        psm.BBM1.setSpeedSync(50)
        sleep(3)
        ninetydegrees(-1)
        psm.BBM1.setSpeedSync(-50)
        sleep(3)
<<<<<<< HEAD
        psm.BBM1.brake()
        psm.BBM2.brake()
=======
        psm.BBM1.brake()
        psm.BBM2.brake()
"""
psm.BBM1.brake()
psm.BBM2.brake()
