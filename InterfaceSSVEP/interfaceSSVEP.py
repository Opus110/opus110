import sys, pygame
from math import *
pygame.init()

size = width, height = 800,600
black = 0,0,0


screen = pygame.display.set_mode(size)
assets = {
	"background":pygame.image.load("backgroundVScroll.png"),
	"leftarrow":pygame.image.load("leftarrow.png"),
	"avatar": pygame.image.load("ball.gif")
}


class BackgroundVScrolling:
	width=0
	height=0
	bg = assets["background"]
	bgRec = bg.get_rect()
	bgRec2 = bg.get_rect()
	bgRec2.top = bgRec.top - bgRec.h
	bgSpeed = [0,1]
	def __init__(self, width, height):
		self.width = width
		self.height = height
		pass
	pass
	def draw(self,screen):
		self.bgRec = self.bgRec.move(self.bgSpeed)
		self.bgRec2 = self.bgRec2.move(self.bgSpeed)
		if self.bgRec.top > self.height:
			self.bgRec.top = 0
			self.bgRec2.top = self.bgRec.top - self.bgRec.h
		screen.blit(self.bg,self.bgRec)	
		screen.blit(self.bg,self.bgRec2)
		pass

class Arrow:
	leftArrow = assets["leftarrow"]	
	width=0
	height=0
	def __init__(self,width, height, left=True):
		self.width = width
		self.height = height
		self.leftArrowRec = self.leftArrow.get_rect()
		self.leftArrowRec.y = (self.height - self.leftArrowRec.h)/2
		if left == False:
			self.leftArrow = pygame.transform.rotate(self.leftArrow,180)
			self.leftArrowRec.x = self.width-self.leftArrowRec.w
		pass
	def draw(self, screen):
		screen.blit(self.leftArrow, self.leftArrowRec)
		pass
	pass

class Avatar:
	sprite = assets["avatar"]
	spriteRect = sprite.get_rect()
	def __init__(self,width, height):
		self.spriteRect.y = (height - self.spriteRect.h)/2
		self.spriteRect.x = (width - self.spriteRect.w)/2
		pass
	def draw(self,screen,mouse):
		speed=[1,0]
		if mouse == 1:
			speed[0] = -1
		if mouse == 0:
			speed[0] = 0
		self.spriteRect = self.spriteRect.move(speed)
		screen.blit(self.sprite,self.spriteRect)
		pass


background =  BackgroundVScrolling(width,height)
leftarrow = Arrow(width,height,True)
rightarrow = Arrow(width,height,False)
avatar = Avatar(width,height)
while 1:
	mouse = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse = event.button
	screen.fill(black)
	background.draw(screen)	
	leftarrow.draw(screen)
	rightarrow.draw(screen)
	avatar.draw(screen,mouse)
	pygame.display.flip()