#!/usr/bin/env python
import RPi.GPIO as GPIO
import random

# display
SDI = 17 
RCLK = 18 
SRCLK = 27

#button
TouchPin = 22

#to get rand for display

#should start num?

num = open('num.log','w')
rando = hex(random.randint(0,15))

def numbo():
    num.write(rando)

def start():
    print('starting the generation')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)
    print('release jorts')
    GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# the 74HC595 chip stuff
def chip(dat):
    for bit in range(0, 15):	
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)
        GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def beep():
    while True:
         if not GPIO.input(TouchPin):
             hc595_shift(num.read())
             time.sleep(2.0)
         hc595_shift(num.read())
         time.sleep(0.060)

#execute on death
def destroy():
    GPIO.cleanup()
    num.close()

#oh god
if __name__ == '__main__':
    numbo()
    start()
    try:
         beep()
    except KeyboardInterrupt:
         destroy()
