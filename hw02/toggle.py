#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
import time
import sys

out = sys.argv[1]
sleepTime = float(sys.argv[2])

print(out)
print(sleepTime)

GPIO.setup(out, GPIO.OUT)

while True:
	GPIO.output(out,GPIO.HIGH)
	time.sleep(sleepTime)
	GPIO.output(out, GPIO.LOW)
	time.sleep(sleepTime)
