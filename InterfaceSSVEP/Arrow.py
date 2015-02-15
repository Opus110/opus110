import pygame
from Assets import assets
from GameState import *



class Arrow:
	leftArrow = assets["leftarrow"]	
	width=0
	height=0
	mustBlink =  False
	frec = None
	T =None
	blinkState = True
	t = 0
	tlast = 0
	def __init__(self,width, height, left=True, frec=0):
		self.width = width
		self.height = height
		self.leftArrow  = pygame.transform.scale(self.leftArrow,(50,50))
		self.leftArrowRec = self.leftArrow.get_rect()
		self.leftArrowRec.y = (self.height - self.leftArrowRec.h)/2
		if left == False:
			self.leftArrow = pygame.transform.rotate(self.leftArrow,180)
			self.leftArrowRec.x = self.width-self.leftArrowRec.w -20
		else:
			self.leftArrowRec.x = 20
		if frec != 0:
			self.mustBlink = True
			self.frec = float(frec)
			self.T = 1/(self.frec*2)			
		pass
	def draw(self, screen, millis, gameState):
		if self.mustBlink and gameState.state == PLAYING:
			seconds = millis / 1000.0 # seconds passed since last frame (float)
			self.t += seconds
			timespan = (self.t-self.tlast)
			if timespan >= self.T:
				self.blinkState = self.blinkState == False
				self.tlast = self.t
				pass
			if self.blinkState :
				screen.blit(self.leftArrow, self.leftArrowRec)
			pass
		else:
			screen.blit(self.leftArrow, self.leftArrowRec)
		pass
	pass