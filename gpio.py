#!/usr/bin/env python
import RPi.GPIO as GPIO

# display
SDI = 17 
RCLK = 18 
SRCLK = 27

#button
TouchPin = 22

#to get rand for display

#should start nano?

num = open('num.log')

def start():
	print 'starting the generation'
  	GPIO.setup(SDI, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(RCLK, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(SRCLK, GPIO.OUT, initial=GPIO.LOW)
	print 'release jorts'
