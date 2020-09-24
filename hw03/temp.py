#!/usr/bin/env python3

#Import libraries
import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

#Set up GPIO pins
GPIO.setup("P9_12", GPIO.IN)
GPIO.setup("P9_11", GPIO.IN)

#Add event detection
GPIO.add_event_detect("P9_12", GPIO.BOTH)
GPIO.add_event_detect("P9_11", GPIO.BOTH)

#Set up the i2c bus
bus = smbus.SMBus(2)

#Set the addresses on the bus
address1 = 0x48
address2 = 0x49

#Loop
while True:
	#print(GPIO.input("P9_12"), end="\n")
	#print(GPIO.input("P9_11"), end="\n")
	#If the first TMP101 goes outside of the range
	if GPIO.event_detected("P9_12"):
		#Read temp and print it
		ctemp1 = bus.read_byte_data(address1, 0)
		ftemp1 = (ctemp1 * 9)/5 + 32
		print("Temperature 1: " + str(ftemp1) + "F or " + str(ctemp1) + "C", end="\n")

	#If the second TMP101 goes outside of the range
	if GPIO.event_detected("P9_11"):
		#Read temp and prnt it
		ctemp2 = bus.read_byte_data(address2, 0)
		ftemp2 = (ctemp2 * 9)/5 + 32
		print("Temperature 2: " + str(ftemp2) + "F or " + str(ctemp2) + "C", end="\n")

	time.sleep(1)



