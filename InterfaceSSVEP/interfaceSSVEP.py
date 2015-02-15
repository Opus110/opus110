import sys, pygame
from math import *
from Assets import assets
from Arrow import Arrow
from BackgroundVScrolling import BackgroundVScrolling
from Avatar import Avatar
from Enemy import Enemy
from ScoreBoard import *
from GameState import GameState


pygame.init()
pygame.font.init()

size = width, height = 800,600
black = 0,0,0
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

gameState =  GameState()

#creating all sprites
allSprites = pygame.sprite.Group()
enemies =  pygame.sprite.Group()
players = pygame.sprite.Group()
scoreboard = pygame.sprite.Group()

background =  BackgroundVScrolling(width,height)
leftarrow = Arrow(width,height,True, frec = 10)
rightarrow = Arrow(width,height,False, frec = 14)
avatar = Avatar(width,height)
scorel = ScoreLabel()
levell = LevelLabel()


for i in range(3):
	enemie =  Enemy((width,height))
	enemie.randomTopPosition()
	enemie.randomSpeed(x=0)
	enemie.moving = True
	enemies.add(enemie)
	allSprites.add(enemie)

allSprites.add(avatar)
players.add(avatar)
scoreboard.add(scorel)
allSprites.add(scorel)
scoreboard.add(levell)
allSprites.add(levell)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gameState.togglePause()	
	screen.fill(black)
	milliseconds = clock.tick()  # milliseconds passed since last frame
	gameState.update()

	#these are not a sprites properly
	background.draw(screen,gameState)	
	leftarrow.draw(screen,milliseconds,gameState)
	rightarrow.draw(screen,milliseconds,gameState)

	players.update(gameState)
	enemies.update(gameState)
	scoreboard.update(gameState)

	allSprites.draw(screen) #draws all sprites
	pygame.display.flip()