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
flag = 0

#trying a new method via interwebs; Number GPIOs by its physical location

def words():
    print('starting the generation')
    print('release jorts')

def start():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(TouchPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(TouchPin, GPIO.RISING, callback = randomISR, bouncetime = 20)


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
	
	
def randomGOD(channel):
    global flag
    flag = 1

def beep():
    global flag
	words()
    while True:
        screen = random.randint(0,15)
        chip(SegCode[screen])
        print screen, hex(SegCode[screen])
        if flag == 1:
            print "Num: ", screen
			num.write(hex(screen)
            time.sleep(2)
            flag = 0
        else:
            time.sleep(0.01)



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
