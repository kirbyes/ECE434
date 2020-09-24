#!/usr/bin/python3

#Setup pygame
import sys, pygame
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

#Setup the Matrix
import smbus
bus = smbus.SMBus(2)
matrix = 0x70
index = [0x80, 0x00, 0x00, 0x00,
	 0x00, 0x00, 0x00, 0x00,
	 0x00, 0x00, 0x00, 0x00,
	 0x00, 0x00, 0x00, 0x00]

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

#Setup the encoders
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
encoder1 = RotaryEncoder(eQEP2)
encoder2 = RotaryEncoder(eQEP1)
encoder1.setAbsolute()
encoder2.setAbsolute()
encoder1.enable()
encoder2.enable()

#Keep track of the previous encoder position
prevPos1 = 0
prevPos2 = 0

#Print instructions
print("Etch-A-Sketch")
print("Move with rotary encoders and clear with spacebar")
print("Move up: Left encoder CCW")
print("Move down: Left encoder CW")
print("Move right: Right encoder CW")
print("Move left: Right encoder CCW")

#Prompt for row and column numbers
rows = 8
columns = 8

#Initialize width and height to be about 500
#Should be exactly divisible by the numer of rows or columns 
size = width, height = int(500/columns)*columns, int(500/rows)*rows
white = (255,255,255)
black = (0,0,0)

#Initialize the screen as a pygame surface
screen = pygame.display.set_mode(size)

#Set cursor
cursorleft = 0
cursortop = 0

#Track the row and column of the cursor
cursorCol = 0
cursorRow = 0

#Function to move the cursor up
def moveup():
	global cursortop,currRow,index,cursorRow
	#If moving will put it outside of the screen, don't do it
	if (cursortop - height/rows) >= 0:
		#Move the cursor
		cursortop = cursortop - height/rows
		cursorRow = cursorRow - 1

#Function to move the cursor down
def movedown():
	global cursortop,currRow,index,cursorRow
	#If moving will put it outside of the screen, don't do it
	if (cursortop + 2 * height/rows) <= width:
		#Move the cursor
		cursortop = cursortop + height/rows
		cursorRow = cursorRow + 1

#Function to move the cursor right
def moveright():
	global cursorleft,currColumn,index,cursorCol
	#If moving will put it outside of the screen, don't do it
	if (cursorleft + 2 * width/columns) <= width:
		#Move the cursor
		cursorleft = cursorleft + width/columns
		cursorCol = cursorCol + 1

#Function to move the cursor left
def moveleft():
	global cursorleft,currColumn,index,cursorCol
	#If moving will put it outside of the screen, don't do it
	if (cursorleft - width/columns) >= 0:
		#Move the cursor
		cursorleft = cursorleft - width/columns
		cursorCol = cursorCol - 1

#Function to clear the screen
def clear():
	global index
	screen.fill(white)
	for i in range (16):
		index[i] = 0

#Initially clear the screen
screen.fill(white)
clear()

#Main loop
while 1:
	#Handle events
	for event in pygame.event.get():
		#Handle quit
		if event.type == pygame.QUIT:
			sys.exit()
		#Handle button presses
		elif event.type == pygame.KEYDOWN:
			#Handle clear
			if event.key == pygame.K_SPACE:
				clear()

	#Handle move left
	if encoder1.position > prevPos1:
		prevPos1 = encoder1.position
		moveleft()
	#Handle move right
	elif encoder1.position < prevPos1:
		prevPos1 = encoder1.position
		moveright()
	#Handle move down
	elif encoder2.position > prevPos2:
		prevPos2 = encoder2.position
		movedown()
	#Handle move up
	elif encoder2.position < prevPos2:
		prevPos2 = encoder2.position
		moveup()

	#Draw the rectangle based on where the cursor is
	pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))

	#Update the screen
	pygame.display.update()

	#Add the cursor position to the column array
	index[(7-cursorCol) * 2] = index[(7-cursorCol) * 2] | (0x01 << cursorRow)
	#Draw the blocks on the matrix
	bus.write_i2c_block_data(matrix, 0, index)
