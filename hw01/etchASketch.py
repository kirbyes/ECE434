#!/usr/bin/env python3
chmod +x

import sys, pygame
pygame.init()
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

print("Etch-A-Sketch")
print("Move with arrow keys and clear with spacebar")

rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

size = width, height = int(500/columns)*columns, int(500/rows)*rows
white = (255,255,255)
black = (0,0,0)

screen = pygame.display.set_mode(size)

cursorleft = 0
cursortop = 0

def moveup():
	global cursortop,currRow,index
	if (cursortop - height/rows) >= 0:
		cursortop = cursortop - height/rows

def movedown():
	global cursortop,currRow,index
	if (cursortop + 2 * height/rows) <= width:
		cursortop = cursortop + height/rows

def moveright():
	global cursorleft,currColumn,index
	if (cursorleft + 2 * width/columns) <= width:
		cursorleft = cursorleft + width/columns

def moveleft():
	global cursorleft,currColumn,index
	if (cursorleft - width/columns) >= 0:
		cursorleft = cursorleft - width/columns

def clear():
	screen.fill(white)

screen.fill(white)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moveup()
			elif event.key == pygame.K_DOWN:
				movedown()
			elif event.key == pygame.K_RIGHT:
				moveright()
			elif event.key == pygame.K_LEFT:
				moveleft()
			elif event.key == pygame.K_SPACE:
				clear()

	pygame.draw.rect(screen,black,(cursorleft,cursortop,width/columns,height/rows))

	pygame.display.update()


