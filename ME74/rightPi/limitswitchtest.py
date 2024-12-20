import RPi.GPIO as GPIO
from time import sleep
import airtable as airtable


SWIN1 = 16 #ground 14
SWIN2 = 18 #ground 20

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)    
    GPIO.setup(SWIN1 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWIN2 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
 


# Pins for Motor Driver Inputs 
Motor1A = 35
Motor1B = 37
Motor1E = 38


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)      # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    
    GPIO.setup(SWIN1 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWIN2 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
def open():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(.1)
    stop()

 
def close():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(.1)
    stop()
 
def stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    print("Stop")

def destroy():  
    GPIO.cleanup()


if __name__ == '__main__':    
    setup()
    try:
        while(True):
            if (GPIO.input(SWIN1) == GPIO.LOW):
                print("bottom unclicked")
            else:
                print("bottom clicked")
            if (GPIO.input(SWIN2) == GPIO.LOW):
                print("top unclicked")
            else:
                print("top clicked")
            sleep(.01)


    except KeyboardInterrupt:
        destroy()