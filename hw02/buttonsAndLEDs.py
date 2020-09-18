#!/usr/bin/env python3

# ///////////////////////////////////
# //
# // Based on /var/lib/cloud9/BeagleBone/Black/input.py
# //
# ///////////////////////////////////

# Imports
import Adafruit_BBIO.GPIO as GPIO
import time

# Initialize pin numbers
led1 = "P9_11";
led2 = "P9_13";
led3 = "P9_15";
led4 = "P9_17";
button1 = "P9_21";
button2 = "P9_23";
button3 = "P9_26";
button4 = "P9_27";

state = 0

# Set up pins as inputs and outputs
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

# Create the callback that chooses which LED to turn on
def button_callback(channel):
	state = GPIO.input(channel)
	print("Edge detected on channel {}, value={}".format(channel, state))
	if channel == button1:
		GPIO.output(led1, state)
	elif channel == button2:
		GPIO.output(led2, state)
	elif channel == button3:
		GPIO.output(led3, state)
	elif channel == button4:
		GPIO.output(led4, state)

#Event detectors for the buttons
GPIO.add_event_detect(button1, GPIO.BOTH, callback=button_callback)
GPIO.add_event_detect(button2, GPIO.BOTH, callback=button_callback)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=button_callback)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=button_callback)

# While loop that runs infinitely until the keyboard interrupts
try:
	while True:
		time.sleep(100)

except KeyboardInterrupt:
	GPIO.cleanup()
