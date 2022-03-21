import pygame as p
import sys as s

from pygame.locals import *

p.init()
display = p.display.set_mode((400, 400))
p.display.set_caption('Hello')

running = True
while running:
	for event in p.event.get():
		if event.type == QUIT:
			p.quit()
			s.exit()
	
	p.display.update()
