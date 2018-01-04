#!/usr/bin/env python
import RPi.GPIO as GPIO

# display
SDI = 17 
RCLK = 18 
SRCLK = 27

#button
TouchPin = 22

#to get rand for display

#should start num?

num = open('num.log')

def start():
	print 'starting the generation'
  	GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)
	print 'release jorts'
	GPIO.setup(TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	
# the 74HC595 chip stuff
def chip(dat):
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
	start()
	setup()
	try:
	     beep()
	except KeyboardInterrupt:
	     destroy()