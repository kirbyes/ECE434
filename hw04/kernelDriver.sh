#!/bin/bash
#Go to the correct flder and initialize devices
cd /sys/class/i2c-adapter/i2c-2
if [ ! -e 2-0048 ]; then
	echo tmp101 0x48 > new_device
fi
if [ ! -e 2-0049 ]; then
	echo tmp101 0x49 > new_device
fi

#Go to the folder for temp 1
cd 2-0048/hwmon/hwmon0
#Save the value
temp1=`cat temp1_input`
#Print out the value with some formatting
echo "scale=2 ; $temp1/1000" | bc
cd ../../..
#Go to the folder for temp 2
cd 2-0049/hwmon/hwmon1
#Save the value
temp2=`cat temp1_input`
#Print out the value with some formatting
echo "scale=2 ; $temp2/1000.0" | bc

