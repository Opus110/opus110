import pygame
from Assets import assets
from GameState import *

class BackgroundVScrolling:
	width=0
	height=0
	bg = assets["background"]
	bgRec = bg.get_rect()
	bgRec2 = bg.get_rect()
	bgRec2.top = bgRec.top - bgRec.h
	bgSpeed = [0,1]
	bgcounter = 0
	def __init__(self, width, height):
		self.width = width
		self.height = height
		pass
	pass
	def draw(self,screen,gameState):
		if gameState.state == PLAYING and self.bgcounter % 5 == 0:
			self.bgRec = self.bgRec.move(self.bgSpeed)
			self.bgRec2 = self.bgRec2.move(self.bgSpeed)
			if self.bgRec.top > self.height:
				self.bgRec.top = 0
				self.bgRec2.top = self.bgRec.top - self.bgRec.h
		self.bgcounter += 1
		screen.blit(self.bg,self.bgRec)	
		screen.blit(self.bg,self.bgRec2)
		pass