import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now

buttonpin = 10
GPIO.setup(buttonpin, GPIO.OUT) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


def buttonpress():
    if GPIO.input(buttonpin) == GPIO.HIGH:
        print("Button was pushed!")
        return False
    else:
        return True

# Define the GPIO pins for the L298N motor driver
# OUT1 = 12
# OUT2 = 11
# OUT3 = 13
# OUT4 = 15

OUT1 = 16
OUT2 = 18
OUT3 = 29
OUT4 = 31

#SPEED based on delay
DELAY = .01

# Set the GPIO pins as output
GPIO.setup(OUT1, GPIO.OUT)
GPIO.setup(OUT2, GPIO.OUT)
GPIO.setup(OUT3, GPIO.OUT)
GPIO.setup(OUT4, GPIO.OUT)


GPIO.output(OUT1,GPIO.LOW)
GPIO.output(OUT2,GPIO.LOW)
GPIO.output(OUT3,GPIO.LOW)
GPIO.output(OUT4,GPIO.LOW)

        
#carries out a (cc) or (c) motion until a limit switch is hit.
def motionup():
    step_delay = DELAY
    current_step = 0    
    total_step = 0 
    while (buttonpress()):
        if current_step == 0:
            GPIO.output(OUT1,GPIO.HIGH)
            GPIO.output(OUT2,GPIO.LOW)
            GPIO.output(OUT3,GPIO.HIGH)
            GPIO.output(OUT4,GPIO.LOW)
            sleep(step_delay)
        elif current_step == 1:
            GPIO.output(OUT1,GPIO.LOW)
            GPIO.output(OUT2,GPIO.HIGH)
            GPIO.output(OUT3,GPIO.HIGH)
            GPIO.output(OUT4,GPIO.LOW)
            sleep(step_delay)
        elif current_step == 2:
            GPIO.output(OUT1,GPIO.LOW)
            GPIO.output(OUT2,GPIO.HIGH)
            GPIO.output(OUT3,GPIO.LOW)
            GPIO.output(OUT4,GPIO.HIGH)
            sleep(step_delay)
        elif current_step == 3:
            GPIO.output(OUT1,GPIO.HIGH)
            GPIO.output(OUT2,GPIO.LOW)
            GPIO.output(OUT3,GPIO.LOW)
            GPIO.output(OUT4,GPIO.HIGH)
            sleep(step_delay)
        if current_step == 3:
            current_step = -1
        current_step = current_step + 1
        total_step = total_step + 1

def motiondown():
    step_delay = DELAY
    current_step = 0
    total_step = 0     
    while (buttonpress()):
        if current_step == 0:
            GPIO.output(OUT1,GPIO.HIGH)
            GPIO.output(OUT2,GPIO.LOW)
            GPIO.output(OUT3,GPIO.HIGH)
            GPIO.output(OUT4,GPIO.LOW)
            sleep(step_delay)
        elif current_step == 1:
            GPIO.output(OUT1,GPIO.HIGH)
            GPIO.output(OUT2,GPIO.LOW)
            GPIO.output(OUT3,GPIO.LOW)
            GPIO.output(OUT4,GPIO.HIGH)
            sleep(step_delay)
        elif current_step == 2:
            GPIO.output(OUT1,GPIO.LOW)
            GPIO.output(OUT2,GPIO.HIGH)
            GPIO.output(OUT3,GPIO.LOW)
            GPIO.output(OUT4,GPIO.HIGH)
            sleep(step_delay)
        elif current_step == 3:
            GPIO.output(OUT1,GPIO.LOW)
            GPIO.output(OUT2,GPIO.HIGH)
            GPIO.output(OUT3,GPIO.HIGH)
            GPIO.output(OUT4,GPIO.LOW)
            sleep(step_delay)
        if current_step == 3:
            current_step = -1
        current_step = current_step + 1
        total_step = total_step + 1

def wait():
    while(buttonpress()):
        sleep(DELAY)

try:
    while(True): 
        wait() 
        sleep(1)
        print("Going up!")
        motionup()
        sleep(1)
        GPIO.output(OUT1,GPIO.LOW)
        GPIO.output(OUT2,GPIO.LOW)
        GPIO.output(OUT3,GPIO.LOW)
        GPIO.output(OUT4,GPIO.LOW)

        wait()
        sleep(1)
        print("Going down!")
        motiondown()
        GPIO.output(OUT1,GPIO.LOW)
        GPIO.output(OUT2,GPIO.LOW)
        GPIO.output(OUT3,GPIO.LOW)
        GPIO.output(OUT4,GPIO.LOW)
        sleep(1)

except KeyboardInterrupt:
    GPIO.output(OUT1,GPIO.LOW)
    GPIO.output(OUT2,GPIO.LOW)
    GPIO.output(OUT3,GPIO.LOW)
    GPIO.output(OUT4,GPIO.LOW)
    print("Exiting the script.")
    GPIO.cleanup()
