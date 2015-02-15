import pygame
from Assets import assets
from GameState import *

debug = False;

class Avatar(pygame.sprite.Sprite):
	def __init__(self,width, height):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.image = assets["avatar"]
		self.rect = self.image.get_rect()
		self.rect.y = self.height - self.rect.h - 50
		self.rect.x = (self.width - self.rect.w)/2
		pass
	def update(self,*args):
		gameState = args[0]
		if gameState.state == PLAYING:
			hspeed = 3
			speed=[hspeed,0]

			mouse =  pygame.mouse.get_pressed()
			if debug:
				print "Pressed buttons :",mouse
			if (mouse[0] == 1 and mouse[2] == 1) == False:
				if mouse[0] == 1:
					speed[0] = -hspeed
				elif mouse[2] == 1:
					speed[0] = hspeed
				else:
					speed[0] = 0
			else:
				speed[0]=0
			
			self.rect = self.rect.move(speed)
			if(self.rect.x < 0):
				self.rect.x = 0
			if(self.rect.x > self.width-self.rect.w ):
				self.rect.x = self.width-self.rect.w
		pass
