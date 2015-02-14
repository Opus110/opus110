#!/usr/bin/python
import sys, pygame
from datetime import time

#Frecuency settings
frec = 10
#frec =  raw_input("Ingrese la frecuencia de parpadeo: ")
frec = float(frec)
print "Frecuencia: ", frec
T = 1/(frec*2)
print "Periodo: ",T
FPS = 24
t=0
tlast = 0
black = 0, 0, 0
white = 255,255,255
blue = 0,0,255
darkblue = 0,0,50
green = 0,255,00
darkgreen = 0,50,0
state = True


#pygame
clock = pygame.time.Clock()
pygame.init()
size = width, height = 300,300
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Frecuencia: '+str(frec)+' Hz')



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
	seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
	t+=seconds
	timespan = (t-tlast)
	screen.fill(black)
	if timespan >= T:
		state = state == False
		tlast = t
		pass	
	if state ==True:
		pygame.draw.circle(screen, darkblue, (width/2, height/2), min(width,height)/3, 0)
	else:
		pygame.draw.circle(screen, blue	, (width/2, height/2), min(width,height)/3, 0)
		
	pygame.display.flip()
	pass
