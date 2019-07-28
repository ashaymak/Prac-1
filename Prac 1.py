#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Ashay Makanjee
Student Number: MKNASH006
Prac: 1
Date: 22/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
status=1
import itertools
chan_list=(26,6,5)
# Logic that you write
def main():
   
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(6,GPIO.OUT,initial=GPIO.LOW)
   GPIO.setup(5,GPIO.OUT,initial=GPIO.LOW)
   GPIO.setup(26,GPIO.OUT,initial=GPIO.LOW) 
   GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
   GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  # for x in range (10):
   #   GPIO.output(chan_list, 1)
    #  time.sleep(1)
     # GPIO.output(chan_list, 0)
   B=itertools.product([0,1], repeat=3)
   for i in itertools.product([0,1], repeat=3):
       GPIO.output(chan_list, i)
       time.sleep(1)
       
           
def swLed(ev=None):
    
    global status
    status = not status
    GPIO.output(chan_list, status)  # switch led status(on-->off; off-->on)

def loop():
    
    GPIO.add_event_detect(23, GPIO.FALLING, callback=swLed, bouncetime=200) # wait for falling and set bouncetime to prevent the callback function from being called multiple times when the button is pressed
    while True:
        time.sleep(1)   # Don't do anything

if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    #main()
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