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

#Function to move the cursor and clear the screen
def move(channel):
	global cursortop, cursorleft, currRow, index, buttonUp, buttonDown, buttonRight, buttonLeft, buttonClear
	#if statement to choose which button was pressed
	if channel == buttonUp:
		print("Up")
		#If moving will put it outside of the screen, don't do it
		if (cursortop - height/rows) >= 0:
			#Move the cursor
			cursortop = cursortop - height/rows
			#Draw the rectangle based on where the cursor is
			pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))
			
	elif channel == buttonDown:
		print("Down")
		#If moving will put it outside of the screen, don't do it
		if (cursortop + 2 * height/rows) <= width:
			#Move the cursor
			cursortop = cursortop + height/rows
			
	elif channel == buttonRight:
		print("Right")
		#If moving will put it outside of the screen, don't do it
		if (cursorleft + 2 * width/columns) <= width:
			#Move the cursor
			cursorleft = cursorleft + width/columns
	
	elif channel == buttonLeft:
		print("Left")
		#If moving will put it outside of the screen, don't do it
		if (cursorleft - width/columns) >= 0:
			#Move the cursor
			cursorleft = cursorleft - width/columns
			
	elif channel == buttonClear:
		print("Clear")
		screen.fill(white)

	#Draw the rectangle based on where the cursor is
	pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))


#Add event Listeners
GPIO.add_event_detect(buttonUp, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonDown, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonRight, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonLeft, GPIO.FALLING, callback=move)
GPIO.add_event_detect(buttonClear, GPIO.FALLING, callback=move)

#Initially clear the screen
screen.fill(white)

# Draw the rectangle initially
pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))

#Main loop
while 1:
	#Handle events
	for event in pygame.event.get():
		#Handle quit
		if event.type == pygame.QUIT:
			sys.exit()
			GPIO.cleanup()

	#Update the screen
	pygame.display.update()
