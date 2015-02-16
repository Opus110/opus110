import pygame
from Assets import colors
from GameState import *

class SpriteText(pygame.sprite.Sprite):
	position = [0,0]
	color = colors["white"]
	margin = 10
	def __init__(self, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.SysFont("", 30)		
		self.screnSize = (width,height)
		pass
	def setPosition(self, x, y):
		self.position = [x,y]
		pass
	def setText(self, text):
		self.image = self.font.render(text, True, self.color)
		self.rect = self.image.get_rect()
		self.rect.x = self.position[0]
		self.rect.y = self.position[1]
		pass
		
	pass


class ScoreLabel(SpriteText):
	position = [0,0]
	def __init__ (self, width, height):
		SpriteText.__init__(self, width, height)		
		self.setText("Score: ")
		self.setPosition(self.margin,height-(self.rect.h+self.margin)*2)
		pass

	def update(self, *args):
		gamestate = args[0]
		text = "Score: "+str(gamestate.score)
		self.setText(text)
		pass
	pass

class LevelLabel(SpriteText):
	position = [0,0]
	def __init__ (self, width, height):
		SpriteText.__init__(self, width, height)		
		self.setText("Level: ")
		self.setPosition(self.margin,height-(self.rect.h+self.margin)*1)
		pass

	def update(self, *args):
		gamestate = args[0]
		text = "Level: "+str(gamestate.level)
		self.setText(text)
		pass
	pass