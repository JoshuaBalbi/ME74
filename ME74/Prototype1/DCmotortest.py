import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 35
Motor1B = 37
Motor1E = 38

Motor2A = 33
Motor2B = 31
Motor2E = 36

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)            # GPIO Numbering
    # GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    # GPIO.setup(Motor1B,GPIO.OUT)
    # GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Motor2A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
 
def loop():
    # Going forwards
    # GPIO.output(Motor1A,GPIO.HIGH)
    # GPIO.output(Motor1B,GPIO.LOW)
    # GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    print("Going forwards")
 
    sleep(2)
    # Going backwards
    # GPIO.output(Motor1A,GPIO.LOW)
    # GPIO.output(Motor1B,GPIO.HIGH)
    # GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    print("Going backwards")
 
    sleep(2)
    # Stop
    # GPIO.output(Motor1E,GPIO.LOW)
    # GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    print("Stop")

def destroy():  
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
            loop()
    except KeyboardInterrupt:
        destroy()