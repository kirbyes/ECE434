#!/usr/bin/env python3

import smbus
import time

bus1 = smbus.SMBus(1)
bus2 = smbus.SMBus(2)

address1 = 0x48
address2 = 0x49

while True:
	ctemp1 = bus1.read_byte_data(address1, 0)
	ctemp2 = bus2.read_byte_data(address2, 0)
	ftemp1 = (ctemp1 * 9)/5 + 32
	ftemp2 = (ctemp2 * 9)/5 + 32
	print("Temperature 1: " + str(ftemp1) + "F or " + str(ctemp1) + "C", end="\n")
	print("Temperature 2: " + str(ftemp2) + "F or " + str(ctemp2) + "C", end="\n")
	print("\n")
	time.sleep(1)


