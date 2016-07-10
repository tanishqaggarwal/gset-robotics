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
purple2 = 11
counter = 0
last_time = datetime.now()
exit = False

def move(direction):
    if direction == "forward":
        psm.BAM1.setSpeed(-100)
        psm.BBM1.setSpeed(-100)
    else:
        psm.BAM1.setSpeed(100)
        psm.BBM1.setSpeed(100)

def brake():
    psm.BAM1.brake()
    psm.BBM1.brake()
    sleep(0.5)

def ninetydegrees(direction):
    if direction == "right":
        s = 1
    else:
        s = -1

    psm.BAM1.setSpeed(s * 100)
    psm.BBM1.setSpeed(s * -100)
    distance(0.3)
    brake()

def touch():
    if (psm.BAS2.isTouchedNXT() and psm.BBS2.isTouchedNXT()):
        return True
    return False

def masontouch():
    if (psm.BAS2.isTouchedNXT() or psm.BBS2.isTouchedNXT()):
        return True
    return False

def distance(feet):
    CONSTANT_MULTIPLIER = 1
    sleep(feet * CONSTANT_MULTIPLIER)

while(not exit):
    light = psm.BAS1.lightSensorNXT(True)
    color = hc.get_colornum()

    if masontouch():
        #Do circumvention routine
        move("backward")
        distance(0.25)
        brake()
        ninetydegrees("right")
        move("forward")
        distance(0.5)
        brake()
        ninetydegrees("left")
        move("forward")
        distance(1.2)
        brake()
        ninetydegrees("left")
        while(psm.BAS1.lightSensorNXT(True) < 550):
            move("forward")
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
                psm.screen.termPrintln("Victim found: total number: " + str(counter))

psm.screen.clearScreen()
psm.screen.termPrintln(str(counter))

psm.led(1, 255, 255, 255)
distance(1)
psm.led(1,0,0,0)

move("forward")
distance(1)
brake()
move("backward")
distance(0.15)
brake()
ninetydegrees("right")

greenfound = False

done = False
print "In stage where it's moving towards right room"
while(not done):
    move("forward")
    color = hc.get_colornum()
    if (color == green or touch()):
        distance(0.5)
        brake()
        done = True
        if (color == green):
            greenfound = True
        break

brake()

if not greenfound:
    t = datetime.now()
    print "In stage where it's moving towards left room"
    done = False
    while(not done):
        move("backward")
        color = hc.get_colornum()
        if (color == purple2 or color == purple): #mason touch for testing purposes
            done = True
            break
        if (color == green):
            distance(0.5)
            done = True
            greenfound = True
            break
	if ((datetime.now() - t).seconds > 15):
	    done = True
            move("forward")
            distance(0.7)
            break

    brake()

    if not greenfound:
        print "Now moving towards central room."
        move("forward")
        distance(0.5)
        brake()
        ninetydegrees("left")
        move("forward")
        distance(0.5)
        brake()

print "Now in green room."
psm.led(1, 0, 255, 0)
distance(1)
psm.led(1,0,0,0)