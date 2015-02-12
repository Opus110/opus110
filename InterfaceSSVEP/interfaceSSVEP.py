import sys, pygame
pygame.init()

size = width, height = 800,600
black = 0,0,0


screen = pygame.display.set_mode(size)

leftArrow = pygame.image.load("leftarrow.png")
leftArrowRec = leftArrow.get_rect()
leftArrowRec.y = (height - leftArrowRec.h)/2
bg =  pygame.image.load("backgroundVScroll.png")
bgRec = bg.get_rect()
bgRec2 = bg.get_rect()
bgRec2.top = bgRec.top - bgRec.h
bgSpeed = [0,1]


while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(black)
	#background scrolling
	bgRec.move(bgSpeed)
	bgRec2.move(bgSpeed)
	screen.blit(bg,bgRec)	
	screen.blit(bg,bgRec2)
	if bgRec.top > height :
		bgRec.top = 0
		bgRec2.top = bgRec.top - bgRec-h


	screen.blit(leftArrow, leftArrowRec)

	pygame.display.flip()