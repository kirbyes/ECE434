#!/usr/bin/python3

# Imports
import Adafruit_BBIO.GPIO as GPIO
import time
import sys

# Parse the arguments
out = sys.argv[1]
sleepTime = float(sys.argv[2])

#Set up the GPIO as an output
GPIO.setup(out, GPIO.OUT)

# Infinite loop to toggle the pin
while True:
	GPIO.output(out,GPIO.HIGH)
	time.sleep(sleepTime)
	GPIO.output(out, GPIO.LOW)
	time.sleep(sleepTime)
