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

def move(direction):
    if direction == "forward":
        psm.BAM1.setSpeed(-100)
        psm.BBM1.setSpeed(-90)
    else:
        psm.BAM1.setSpeed(100)
        psm.BBM1.setSpeed(90)

def ninetydegrees(direction):
    if direction == "right":
        s = -1
    else:
        s = 1

def touch():
    if psm.BAS2.isTouchedEV3() and psm.BAS1.isTouchedEV3():
        return True
    return False

def masontouch():
    if psm.BAS2.isTouchedEV3() or psm.BAS1.isTouchedEV3():
        return True
    return False

    psm.BAM1.setSpeed(s * 50)
    psm.BBM1.setSpeed(s * -50)
    sleep(0.285)
    psm.BBM1.brake()
    psm.BAM1.brake()

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    color = hc.get_colornum()

    if masontouch():
        #Do circumvention routine
        move("backward")
        sleep(0.5)
        ninetydegrees("right")
        move("forward")
        sleep(1)
        ninetydegrees("left")
        move("forward")
        sleep(0.5)
        ninetydegrees("right")
    else:
        #line follow, victim track
        if(light <= 550):
            psm.BBM1.brake()
            psm.BAM1.setSpeed(-50)
        else:
            psm.BAM1.setSpeed(25)
            psm.BBM1.setSpeed(-50)
        if(color == red or color == red2):
            psm.BBM1.brake()
            psm.BAM1.brake()
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
            psm.BAM1.brake()
            psm.BBM1.brake()
            exit = True

psm.led(1, 255, 255, 255)
sleep(1)
psm.led(1,0,0,0)

move("forward")
sleep(2.5)
move("backward")
sleep(0.1)
ninetydegrees("right")

greenfound = False

t = datetime.now()
done = False
while(not done):
    move("forward")
    color = hc.get_colornum()
    if (color == green or if touch()):
        sleep(0.5)
        psm.BAM1.brake()
        psm.BBM1.brake()
        done = True
        if (color == green):
            greenfound = True
        break

if not greenfound:
    t = datetime.now()
    done = False
    while(not done):
        psm.BAM1.setSpeedSync(-50)
        color = hc.get_colornum()
        if (color == green or touch()):
            sleep(0.5)
            psm.BAM1.brake()
            psm.BBM1.brake()
            done = True
            if (color == green):
                greenfound = True
            break

    if not greenfound:
        move("backward")
        sleep(3)
        ninetydegrees("left")
        move("forward")
        sleep(3)
        psm.BAM1.brake()
        psm.BBM1.brake()

