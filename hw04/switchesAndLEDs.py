#!/usr/bin/env python3

from mmap import mmap
import time, struct

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
GPIO_DATAIN = 0x138

GPIO0_offset = 0x44e07000
GPIO0_size = 0x44e07fff-GPIO0_offset

USR3 = 1<<24
USR1 = 1<<22
button1 = 1<<16
button2 = 1<<31


with open("/dev/mem", "r+b") as f:
	mem0 = mmap(f.fileno(), GPIO0_size, offset=GPIO0_offset)
	mem1 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

packed_reg = mem1[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(USR3)
reg_status &= ~(USR1)
mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

try:
	while(True):
		if ((int.from_bytes(mem1[GPIO_DATAIN:GPIO_DATAIN+4], byteorder='big')>>8)&1) == 0:
			mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR3)
		if ((int.from_bytes(mem1[GPIO_DATAIN:GPIO_DATAIN+4], byteorder='big')>>8)&1):
			mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR3)
		if ((int.from_bytes(mem0[GPIO_DATAIN:GPIO_DATAIN+4], byteorder='big')>>7)&1) == 0:
			mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR1)
		if ((int.from_bytes(mem0[GPIO_DATAIN:GPIO_DATAIN+4], byteorder='big')>>7)&1):
			mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR1)

except KeyboardInterrupt:
	mem0.close()
	mem1.close()
