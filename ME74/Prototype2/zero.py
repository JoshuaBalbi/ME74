import RPi.GPIO as GPIO
from time import sleep
import Final.airtable as airtable

# Pins for Motor Driver Inputs 
Motor1A = 35
Motor1B = 37
Motor1E = 38

Motor2A = 33
Motor2B = 31
Motor2E = 36

SWIN1 = 18 #ground 14
SWIN2 = 16 #ground 20

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)            # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
    GPIO.setup(SWIN1 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(SWIN2 , GPIO.IN, pull_up_down=GPIO.PUD_UP)
 

 
def closeleft():
    print("going down")
    while (GPIO.input(SWIN2) == GPIO.HIGH):
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)
    stop()
 

def closeright():
    print("going down")
    while (GPIO.input(SWIN1) == GPIO.HIGH):
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)
    stop()


def stop():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    print("Stop")

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':    
    setup()
    try:
        closeleft()
        sleep(5)
        closeright()
    except KeyboardInterrupt:
        destroy()