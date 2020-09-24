#!/bin/bash

#Set up P9_11 as gpio if it isn't
if [ ! -e /sys/class/gpio/gpio30 ]; then
	echo "30" > /sys/class/gpio/export
fi
#Set P9_11 as input
echo "in" > /sys/class/gpio/gpio30/direction

#Set up P9_12 as gpio if it isn't
if [ ! -e /sys/class/gpio/gpio60 ]; then
	echo "30" > /sys/class/gpio/export
fi
#Set P9_12 as gpio if it isn't
echo "in" > /sys/class/gpio/gpio60/direction

#Loop
while true
do
	#Set the temp limits
	i2cset -y 2 0x48 3 25
	i2cset -y 2 0x48 2 23
	alert1=`cat /sys/class/gpio/gpio60/value`

	i2cset -y 2 0x49 3 25
	i2cset -y 2 0x49 2 23
	alert2=`cat /sys/class/gpio/gpio30/value`

	printf "$alert1\n"
	printf "$alert2\n"

	#Get the temp
	temp1=`i2cget -y 2 0x48 00`
	temp2=`i2cget -y 2 0x49 00`

	#Convert
	ftemp1=$((($temp1*9/5)+32))
	ftemp2=$((($temp2*9/5)+32))

	#Print out the temp
	printf "Temperature 1: $ftemp1 F or %d C\n" $temp1
	printf "Temperature 2: $ftemp2 F or %d C\n" $temp2
	printf "\n"

	sleep 1
done
