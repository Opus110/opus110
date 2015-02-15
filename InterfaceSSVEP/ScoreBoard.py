import pygame
from Assets import colors
from GameState import *



class ScoreLabel(pygame.sprite.Sprite):
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.SysFont("", 30)		
		self.image = self.font.render("Score: 0", True, colors["red"])
		self.rect = self.image.get_rect()
		
		pass
	def setPosition(self, x, y):
		self.rect.y = 100
		self.rect.x = 100
		pass

	def update(self, *args):
		gamestate = args[0]
		self.image = self.font.render("Score: "+str(gamestate.score), True, colors["red"])
		self.rect = self.image.get_rect()

		pass
	pass

class LevelLabel(pygame.sprite.Sprite):
	position = (0,0)
	def __init__ (self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.SysFont("", 30)		
		self.image = self.font.render("Level: 1", True, colors["black"])
		self.rect = self.image.get_rect()
		self.setPosition(100,200)
		pass
	def setPosition(self, x, y):
		self.position = (x,y)
		pass

	def update(self, *args):
		gamestate = args[0]
		self.image = self.font.render("Level: "+str(gamestate.level), True, colors["black"])
		self.rect = self.image.get_rect()
		self.rect.x = self.position[0]
		self.rect.y = self.position[1]

		pass
	pass