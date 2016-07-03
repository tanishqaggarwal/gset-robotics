from PiStorms import PiStorms
from time import sleep
print "running program"
psm=PiStorms()



#exit variable will be used later to exit the program and return to PiStorms
exit=False
black=700
white=400
leftinit=(-50)    #motor value when see black
leftrange=(-50)   #motor value + init when see black
rightinit=(-25)
rightrange=(75)


average=(black+white)/2
width=(black-white)/2*1.1

while(not exit):
    light=psm.BAS1.lightSensorNXT(True)
    proportions=(light-average)/width
    psm.BAM1.setSpeed(rightinit+proportions*rightrange)
    psm.BAM2.setSpeed(leftspeed+proportions*leftrange)

    psm.led(1,255,0,255) 
    sleep(0.1)

    if(psm.isKeyPressed()): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("")
        psm.screen.termPrintln("Exiting to menu")
        psm.led(1,0,0,0)

        psm.BAM1.brake()
        psm.BAM2.brake()
        sleep(0.5)
        exit = True