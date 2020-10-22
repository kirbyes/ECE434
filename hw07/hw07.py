#!/usr/bin/env python3
# From: https://github.com/blynkkk/lib-python
# Blink the USR3 LED in response to a V0 input.
import blynklib
import blynktimer
import smbus
import os, sys
import Adafruit_BBIO.GPIO as GPIO

# Get the autherization code (See setup.sh)
BLYNK_AUTH = os.getenv('BLYNK_AUTH', default="")
BLYNK_AUTH = "GDQ4D5GkUm3Al4rzXRYqKxsicKuFircB"
if(BLYNK_AUTH == ""):
    print("BLYNK_AUTH is not set")
    sys.exit()

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)
timer = blynktimer.Timer()

#Set up the i2c bus
bus = smbus.SMBus(2)

#Set up matrix values
matrix = 0x70
indexHold = [0x80, 0x00, 0x00, 0x00,
	 0x00, 0x00, 0x00, 0x00,
	 0x00, 0x00, 0x00, 0x00,
	 0x00, 0x00, 0x00, 0x00]

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

#Set the addresses on the bus
address1 = 0x49

rows = 8
columns = 8

#Set up timer
@timer.register(vpin_num=10, interval=1, run_once=False)

#Loop
def write_to_virtual_pin(vpin_num=10):
	ctemp = bus.read_byte_data(address1, 0)
	blynk.virtual_write(10, ctemp)

#Track the row and column of the cursor
cursorCol = 0
cursorRow = 0

#Function to move the cursor up
def moveup():
	global indexHold,cursorRow,cursorCol,matrix
	#If moving will put it outside of the screen, don't do it
	if cursorRow > 0:
		#Move the cursor
		cursorRow = cursorRow - 1
		#Add the cursor position to the column array
		indexHold[(7-cursorCol) * 2] = indexHold[(7-cursorCol) * 2] | (0x01 << cursorRow)
		#Draw the blocks on the matrix
		bus.write_i2c_block_data(matrix, 0, indexHold)


#Function to move the cursor down
def movedown():
	global indexHold,cursorRow,cursorCol,matrix
	#If moving will put it outside of the screen, don't do it
	if cursorRow < (rows - 1):
		#Move the cursor
		cursorRow = cursorRow + 1
		#Add the cursor position to the column array
		indexHold[(7-cursorCol) * 2] = indexHold[(7-cursorCol) * 2] | (0x01 << cursorRow)
		#Draw the blocks on the matrix
		bus.write_i2c_block_data(matrix, 0, indexHold)


#Function to move the cursor right
def moveright():
    global indexHold,cursorCol,cursorRow,matrix
    #If moving will put it outside of the screen, don't do it
    if cursorCol < (columns - 1):
        print("Here")
        #Move the cursor
        cursorCol = cursorCol + 1
        #Add the cursor position to the column array
        indexHold[(7-cursorCol) * 2] = indexHold[(7-cursorCol) * 2] | (0x01 << cursorRow)
        #Draw the blocks on the matrix
        bus.write_i2c_block_data(matrix, 0, indexHold)


#Function to move the cursor left
def moveleft():
	global indexHold,cursorCol,cursorRow,matrix
	#If moving will put it outside of the screen, don't do it
	if cursorCol > 0:
		#Move the cursor
		cursorCol = cursorCol - 1
		#Add the cursor position to the column array
		indexHold[(7-cursorCol) * 2] = indexHold[(7-cursorCol) * 2] | (0x01 << cursorRow)
		#Draw the blocks on the matrix
		bus.write_i2c_block_data(matrix, 0, indexHold)


#Function to clear the screen
def clear():
	global indexHold,cursorCol,cursorRow,matrix
#	screen.fill(white)
	for i in range (16):
		indexHold[i] = 0
	#Add the cursor position to the column array
	indexHold[(7-cursorCol) * 2] = indexHold[(7-cursorCol) * 2] | (0x01 << cursorRow)
	#Draw the blocks on the matrix
	bus.write_i2c_block_data(matrix, 0, indexHold)

#Clear the LED Matrix
clear()

#Get the button presses from the app
@blynk.handle_event('write V*')
def my_write_handler(pin, value):
    print('Current V{} value: {}'.format(pin, value))
    if value == ["1"]:
        if pin == 0:
            moveup()
        elif pin == 1:
            movedown()
        elif pin == 2:
            moveright()
        elif pin == 3:
            moveleft()
        elif pin == 4:
            clear()

while True:
    blynk.run()
    timer.run()
