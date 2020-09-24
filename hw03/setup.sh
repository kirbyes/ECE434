#!/bin/bash

#Temperature

#Give the python script permissions
chmod +x temp.py

#Check if P9_11 exist as gpio, if not set it
if [ ! -e /sys/class/gpio/gpio30 ]; then
	echo "30" > /sys/class/gpio/export
fi
#Set the pin as an input
echo "in" > /sys/class/gpio/gpio30/direction

#Check if P9_12 exist as gpio, if not set it
if [ ! -e /sys/class/gpio/gpio60 ]; then
	echo "60" > /sys/class/gpio/export
fi
#Set the pin as an input
echo "in" > /sys/class/gpio/gpio60/direction

#Set the Thigh to be 26C for the first TMP101
i2cset -y 2 0x48 3 26
#Set the Tlow to be 23C for the first TMP101
i2cset -y 2 0x48 2 24

#Set the Thigh to be 26C for the second TMP101
i2cset -y 2 0x49 3 26
#Set the Tlow to be 23C for the second TMP101
i2cset -y 2 0x49 2 24




#Etch-A-Sketch
#Configure the pins to eqep
config-pin P8_11 eqep
config-pin P8_12 eqep
config-pin P8_33 eqep
config-pin P8_35 eqep
