#!/usr/bin/python3
"""
Ashay Makanjee
Student Number: MKNASH006
Prac: 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
import itertools
counter=0
chan_list=(26,6,5)#list of pins for LEDs
GPIO.setmode(GPIO.BCM)# set pin numbering to BCM
#Setting each pin to either input or output
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(26,GPIO.OUT) 
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#Makes a list of the binary values from 0 to 7
B=list(itertools.product([0,1], repeat=3)) 

def main(ev=None):#function that uses interrupts to detect button presses, with debouncing
    GPIO.add_event_detect(24, GPIO.FALLING, callback=button_up, bouncetime=200)#up count
    GPIO.add_event_detect(23, GPIO.FALLING, callback=button_down, bouncetime=200)#down count
    while True:
        time.sleep(1)
        
def button_up(ev=None):#function that is used when counting up
    global counter#global variable used for counter for all the functions
    if (counter==7):#loop used for wrap around
        counter=0
    else:
        counter=counter+1
    
    GPIO.output(chan_list, B[counter])
    
    
def button_down(ev=None):#used when counting down
    global counter
    if (counter==0):
        counter=7
    else:
        counter=counter-1
    
    GPIO.output(chan_list, B[counter])
       

if __name__ == "__main__":
    
    try:
        while True:
         main()  # run the function continuously 
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
