
#!/bin/bash
config-pin P9_17 i2c
config-pin P9_18 i2c
config-pin P9_21 i2c
config-pin P9_22 i2c

while true
do
	temp1=`i2cget -y 1 0x48 00`
	temp2=`i2cget -y 2 0x49 00`
	ctemp1=$(((($temp1>>4)*16)+($temp1&0xf)))
	ctemp2=$(((($temp2>>4)*16)+($temp2&0xf)))
	ftemp1=$((($ctemp1*9/5)+32))
	ftemp2=$((($ctemp2*9/5)+32))
	printf "Temperature 1: $ftemp1 F or $ctemp1 C\n"
	printf "Temperature 2: $ftemp2 F or $ctemp2 C\n"
	printf "\n"
	sleep 1
done
