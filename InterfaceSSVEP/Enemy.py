import pygame
import random
from Assets import assets
from GameState import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self, screnSize):
		pygame.sprite.Sprite.__init__(self)	
		self.screnSize = screnSize
		self.image = assets["enemy"]
		self.image = pygame.transform.rotate(self.image,180)
		self.image = pygame.transform.scale(self.image,(50,50))
		self.rect = self.image.get_rect()
		self.moving =  True
		pass
	def randomTopPosition(self, verticaloffset = -400):
		width =  self.screnSize[0]
		pos = (random.randrange(width-self.rect.w),random.randrange(verticaloffset,0))
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		pass
	def randomSpeed(self,x=0,y=0):
		yval = random.randrange(1,5)*random.randrange(100)/100
		yval = 1 if yval<1 else yval
		self.speed =[0, yval ]
		if(x != 0):
			self.speed[0] = x
		if(x != 0):
			self.speed[1] = y
		pass
	def update(self, *args):
		gameState = args[0]
		if gameState.state == PLAYING and self.moving: 
			if self.rect.y >  self.screnSize[1]:
				self.randomTopPosition()
				self.randomSpeed(x=0)
			self.rect = self.rect.move(self.speed)

		pass
	pass