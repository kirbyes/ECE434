#!/bin/bash
cd /sys/class/i2c-adapter/i2c-2
if [ ! -e 2-0048 ]; then
	echo tmp101 0x48 > new_device
fi
if [ ! -e 2-0049 ]; then
	echo tmp101 0x49 > new_device
fi

cd 2-0048/hwmon/hwmon0
temp1=`cat temp1_input`
echo "scale=2 ; $temp1/1000" | bc
cd ../../..
cd 2-0049/hwmon/hwmon1
temp2=`cat temp1_input`
echo "scale=2 ; $temp2/1000.0" | bc

