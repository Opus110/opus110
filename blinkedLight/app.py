import sys, pygame
from datetime import time

frec =  raw_input("Ingrese la frecuencia de parpadeo: ")
frec = float(frec)
print "Frecuencia: ", frec
T = 1/(frec*2)
print "Periodo: ",T
FPS = 24
t=0
tlast = 0
#pigame
clock = pygame.time.Clock()
pygame.init()
size = width, height = 200,200
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = 255,255,255
state = True
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	milliseconds = clock.tick(FPS)  # milliseconds passed since last frame
	seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
	t+=seconds
	timespan = (t-tlast)

	if timespan >= T:
		if state ==True:
			screen.fill(black)
		else:
			screen.fill(white)
		state = state == False
		#print state
		tlast = t
		pass	
		
	pygame.display.flip()
	pass
