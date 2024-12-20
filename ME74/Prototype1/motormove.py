import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

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
    while (total_step < 1000):
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
    while (total_step < 1000):
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


try:  
    print("Going up!")
    motionup()
    GPIO.output(OUT1,GPIO.LOW)
    GPIO.output(OUT2,GPIO.LOW)
    GPIO.output(OUT3,GPIO.LOW)
    GPIO.output(OUT4,GPIO.LOW)
    sleep(5)

    print("Going down!")
    motiondown()
    GPIO.output(OUT1,GPIO.LOW)
    GPIO.output(OUT2,GPIO.LOW)
    GPIO.output(OUT3,GPIO.LOW)
    GPIO.output(OUT4,GPIO.LOW)
    sleep(5)
except KeyboardInterrupt:
    GPIO.output(OUT1,GPIO.LOW)
    GPIO.output(OUT2,GPIO.LOW)
    GPIO.output(OUT3,GPIO.LOW)
    GPIO.output(OUT4,GPIO.LOW)
    print("Exiting the script.")
    GPIO.cleanup()
