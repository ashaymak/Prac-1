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
chan_list=(26,6,5)
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(26,GPIO.OUT) 
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
B=list(itertools.product([0,1], repeat=3)) 

def main(ev=None):
    GPIO.add_event_detect(24, GPIO.FALLING, callback=button_up, bouncetime=200)
    GPIO.add_event_detect(23, GPIO.FALLING, callback=button_down, bouncetime=200)
    while True:
        time.sleep(1)
        
def button_up(ev=None):
    global counter
    if (counter==7):
        counter=0
    else:
        counter=counter+1
    
    GPIO.output(chan_list, B[counter])
    
    
def button_down(ev=None):
    global counter
    if (counter==0):
        counter=7
    else:
        counter=counter-1
    
    GPIO.output(chan_list, B[counter])
       

if __name__ == "__main__":
    
    try:
        while True:
         main()   
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
  #  except c:
   #     GPIO.cleanup()
      #  print("Some other error occurred")
     #   print(c.message)
