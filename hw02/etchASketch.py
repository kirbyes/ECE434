#!/usr/bin/python3

#Import GPIO and time
import Adafruit_BBIO.GPIO as GPIO
import time

#Setup pygame
import sys, pygame
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

#Set up GPIO
buttonUp = "P9_21"
buttonDown = "P9_23"
buttonRight = "P9_26"
buttonLeft = "P9_27"
buttonClear = "P9_30"

GPIO.setup(buttonUp, GPIO.IN)
GPIO.setup(buttonDown, GPIO.IN)
GPIO.setup(buttonRight, GPIO.IN)
GPIO.setup(buttonLeft, GPIO.IN)
GPIO.setup(buttonClear, GPIO.IN)

#Print instructions
print("Etch-A-Sketch")
print("Move and clear with buttons")

#Prompt for row and column numbers
rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

#Initialize width and height to be about 500
#Should be exactly divisible by the number of rows or columns
size = width, height = int(500/columns)*columns, int(500/rows)*rows
white = (255,255,255)
black = (0,0,0)

#Initialize the screen as a pygame surface
screen = pygame.display.set_mode(size)

#Set cursor
cursorleft = 0
cursortop = 0

#Function to move the cursor up
def moveup(channel):
	print("Up")
	global cursortop,currRow,index
	#If moving will put it outside of the screen, don't do it
	if (cursortop - height/rows) >= 0:
		#Move the cursor
		cursortop = cursortop - height/rows

#Function to move the cursor down
def movedown(channel):
	print("Down")
	global cursortop,currRow,index
	#If moving will put it outside of the screen, don't do it
	if (cursortop + 2 * height/rows) <= width:
		#Move the cursor
		cursortop = cursortop + height/rows

#Function to move the cursor right
def moveright(channel):
	print("Right")
	global cursorleft,currColumn,index
	#If moving will put it outside of the screen, don't do it
	if (cursorleft + 2 * width/columns) <= width:
		#Move the cursor
		cursorleft = cursorleft + width/columns

#Function to move the cursor left
def moveleft(channel):
	print("Left")
	global cursorleft,currColumn,index
	#If moving will put it outside of the screen, don't do it
	if (cursorleft - width/columns) >= 0:
		#Move the cursor
		cursorleft = cursorleft - width/columns

#Function to clear the screen
def clear(channel):
	print("Clear")
	screen.fill(white)

#Add event Listeners
GPIO.add_event_detect(buttonUp, GPIO.FALLING, callback=moveup, bouncetime=200)
GPIO.add_event_detect(buttonDown, GPIO.FALLING, callback=movedown, bouncetime=200)
GPIO.add_event_detect(buttonRight, GPIO.FALLING, callback=moveright, bouncetime=200)
GPIO.add_event_detect(buttonLeft, GPIO.FALLING, callback=moveleft, bouncetime=200)
GPIO.add_event_detect(buttonClear, GPIO.FALLING, callback=clear, bouncetime=200)

#Initially clear the screen
screen.fill(white)

#Main loop
while 1:
	#Handle events
	for event in pygame.event.get():
		#Handle quit
		if event.type == pygame.QUIT:
			sys.exit()
			GPIO.cleanup()
#			#Handle button presses
#			elif event.type == pygame.KEYDOWN:
#				#Handle UP arrow
#				if event.key == pygame.K_UP:
#					moveup()
#				#Handle DOWN arrow
#				elif event.key == pygame.K_DOWN:
#					movedown()
#				#Handle right arrow
#				elif event.key == pygame.K_RIGHT:
#					moveright()
#				#Handle left arrow
#				elif event.key == pygame.K_LEFT:
#					moveleft()
#				#Handle SPACEBAR
#				elif event.key == pygame.K_SPACE:
#					clear()

	#Draw the rectangle based on where the cursor is
	pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))

	#Update the screen
	pygame.display.update()
