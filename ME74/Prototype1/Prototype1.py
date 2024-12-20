import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # Ignore warning for now

buttonpin = 10
GPIO.setup(buttonpin, GPIO.OUT) # Set pin 10 to be an input pin and set initial value to be pulled low (off)


# Define the GPIO pins for the L298N motor driver
OUT11 = 12
OUT21 = 11 
OUT31 = 13
OUT41 = 15

OUT12 = 16
OUT22 = 18
OUT32 = 29
OUT42 = 31

#SPEED based on delay
DELAY = .01

# Set the GPIO pins as output
GPIO.setup(OUT11, GPIO.OUT)
GPIO.setup(OUT21, GPIO.OUT)
GPIO.setup(OUT31, GPIO.OUT)
GPIO.setup(OUT41, GPIO.OUT)
GPIO.setup(OUT12, GPIO.OUT)
GPIO.setup(OUT22, GPIO.OUT)
GPIO.setup(OUT32, GPIO.OUT)
GPIO.setup(OUT42, GPIO.OUT)


        
#motor going upwards until button is pressed
def motionup():
    current_step = 0    
    total_step = 0 
    while (buttonpress()):
        if current_step == 0:
            stepzero()
        elif current_step == 1:
            stepone()
        elif current_step == 2:
            steptwo()
        elif current_step == 3:
            stepthree()
        if current_step == 3:
            current_step = -1
        current_step = current_step + 1
        total_step = total_step + 1
    stop()

#motor going downwards until button is pressed
def motiondown():
    current_step = 0
    total_step = 0     
    while (buttonpress()):
        if current_step == 0:
            stepzero()
        elif current_step == 1:
            stepthree()
        elif current_step == 2:
            steptwo()
        elif current_step == 3:
            stepone()
        if current_step == 3:
            current_step = -1
        current_step = current_step + 1
        total_step = total_step + 1
    stop()


def stepzero():
    #motor1
    GPIO.output(OUT11,GPIO.HIGH)
    GPIO.output(OUT21,GPIO.LOW)
    GPIO.output(OUT31,GPIO.HIGH)
    GPIO.output(OUT41,GPIO.LOW)
    #motor2 
    GPIO.output(OUT12,GPIO.HIGH)
    GPIO.output(OUT22,GPIO.LOW)
    GPIO.output(OUT32,GPIO.HIGH)
    GPIO.output(OUT42,GPIO.LOW)
    sleep(DELAY)

def stepone():
    #motor1
    GPIO.output(OUT11,GPIO.LOW)
    GPIO.output(OUT21,GPIO.HIGH)
    GPIO.output(OUT31,GPIO.HIGH)
    GPIO.output(OUT41,GPIO.LOW)
    #motor2 
    GPIO.output(OUT12,GPIO.LOW)
    GPIO.output(OUT22,GPIO.HIGH)
    GPIO.output(OUT32,GPIO.HIGH)
    GPIO.output(OUT42,GPIO.LOW)
    sleep(DELAY)

def steptwo():
    #motor1
    GPIO.output(OUT11,GPIO.LOW)
    GPIO.output(OUT21,GPIO.HIGH)
    GPIO.output(OUT31,GPIO.LOW)
    GPIO.output(OUT41,GPIO.HIGH)
    #motor2 
    GPIO.output(OUT12,GPIO.LOW)
    GPIO.output(OUT22,GPIO.HIGH)
    GPIO.output(OUT32,GPIO.LOW)
    GPIO.output(OUT42,GPIO.HIGH)
    sleep(DELAY)

def stepthree():
    #motor1
    GPIO.output(OUT11,GPIO.HIGH)
    GPIO.output(OUT21,GPIO.LOW)
    GPIO.output(OUT31,GPIO.LOW)
    GPIO.output(OUT41,GPIO.HIGH)
    #motor2 
    GPIO.output(OUT12,GPIO.HIGH)
    GPIO.output(OUT22,GPIO.LOW)
    GPIO.output(OUT32,GPIO.LOW)
    GPIO.output(OUT42,GPIO.HIGH)
    sleep(DELAY)

def buttonpress():
    if GPIO.input(buttonpin) == GPIO.HIGH:
        print("Button was pushed!")
        return False
    else:
        return True
    
def wait():
    while(buttonpress()):
        sleep(DELAY)

def stop():
    GPIO.output(OUT11,GPIO.LOW)
    GPIO.output(OUT21,GPIO.LOW)
    GPIO.output(OUT31,GPIO.LOW)
    GPIO.output(OUT41,GPIO.LOW)
    GPIO.output(OUT12,GPIO.LOW)
    GPIO.output(OUT22,GPIO.LOW)
    GPIO.output(OUT32,GPIO.LOW)
    GPIO.output(OUT42,GPIO.LOW)


try:  
    while True:
        wait() 
        sleep(1)
        print("Going up!")
        motionup()
        sleep(1)
        stop()

        wait()
        sleep(1)
        print("Going down!")
        motiondown()
        stop()
        sleep(1)
except KeyboardInterrupt:
    stop()
    print("Exiting the script.")
    GPIO.cleanup()
