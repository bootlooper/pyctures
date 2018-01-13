#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import random
from random import randint

# display
#was pin no wrong?
SDI   = 17
RCLK  = 18
SRCLK = 27
#button
TouchPin = 22

#to get rand for display

#should start num?

lights = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

num = open('num','w+')
rando = random.choice(lights)

#trying a new method via interwebs; Number GPIOs by its physical location

def start():
    print('starting the generation')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)
    print('release jorts')

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
#         if not GPIO.input(TouchPin):
#             chip(lights[randint(0,15)])
#             time.sleep(2.0)
#         chip(lights[randint(0,15)])
#         time.sleep(0.060)

          for q in range(0, len(lights)):
                chip(lights[q])
                time.sleep(0.5)
#                num.write(lights[q])

#execute on death
def destroy():
    GPIO.cleanup()
    num.close()

#oh god
if __name__ == '__main__':
    start()
    try:
         beep()
    except KeyboardInterrupt:
         destroy()
