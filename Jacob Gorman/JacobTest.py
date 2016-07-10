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

def brake():
    psm.BAM1.brake()
    psm.BBM1.brake()

def ninetydegrees(direction):
    if direction == "right":
        s = 1
    else:
        s = -1

    psm.BAM1.setSpeed(s * 50)
    psm.BBM1.setSpeed(s * -50)
    sleep(0.285)
    brake()

def touch():
    if (psm.BAS2.isTouchedNXT() and psm.BBS2.isTouchedNXT()):
        return True
    return False

def masontouch():
    if (psm.BAS2.isTouchedNXT() or psm.BBS2.isTouchedNXT()):
        return True
    return False


while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    color = hc.get_colornum()

    if masontouch():
        #Do circumvention routine
        move("backward")
        sleep(0.5)
        brake()
        ninetydegrees("right")
        move("forward")
        sleep(1)
        brake()
        ninetydegrees("left")
        move("forward")
        sleep(1.5)
        brake()
        ninetydegrees("left")
        move("forward")
        sleep(0.4)
        brake()
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
            brake()
            psm.screen.clearScreen()
            psm.screen.termPrintln(str(counter))
            exit = True
        elif(color == blue or color == green):
            if((datetime.now() - last_time).seconds > 0):
                counter += 1
                last_time = datetime.now()
                psm.screen.clearScreen()
                psm.screen.termPrintln("I'm functioning Properly")

psm.screen.clearScreen()
psm.screen.termPrintln(str(counter))

psm.led(1, 255, 255, 255)
sleep(1)
psm.led(1,0,0,0)

move("forward")
sleep(2.5)
brake()
move("backward")
sleep(0.3)
brake()
ninetydegrees("right")

greenfound = False

done = False
print "In stage where it's moving towards right room"
while(not done):
    move("forward")
    color = hc.get_colornum()
    if (color == green or touch()):
        sleep(0.5)
        brake()
        done = True
        if (color == green):
            greenfound = True
        break

brake()

if not greenfound:

    print "In stage where it's moving towards left room"
    done = False
    while(not done):
        move("backward")
        color = hc.get_colornum()
        if (color == purple):
            done = True
            break
        if (color == green):
            sleep(0.5)
            done = True
            greenfound = True
            break

    brake()

    if not greenfound:
        print "Now moving towards central room."
        move("forward")
        sleep(3)
        brake()
        ninetydegrees("left")
        move("forward")
        sleep(0.5)
        brake()

print "Now in green room."
