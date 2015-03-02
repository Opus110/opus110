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
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Opus 110")
clock = pygame.time.Clock()
black = colors["black"]
gameState =  GameState()

#creating all sprites
allSprites = pygame.sprite.Group()
enemies =  pygame.sprite.Group()
players = pygame.sprite.Group()

#creating all game objects
background =  BackgroundVScrolling(width,height)
leftarrow = Arrow(width,height,True, frec = 10)
rightarrow = Arrow(width,height,False, frec = 14)
avatar = Avatar(width,height)
scoreboard = ScoreBoard(width,height)

for i in range(3):
	enemy =  Enemy((width,height))
	enemy.randomTopPosition()
	enemy.randomSpeed(x=0)
	enemy.moving = True
	enemies.add(enemy)
	allSprites.add(enemy)

allSprites.add(avatar)
players.add(avatar)
avatar.allSprites = allSprites

#Game loop
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
	#Other shapes or sprites
	background.draw(screen,gameState)	
	

	#sprites
	players.update(gameState)
	enemies.update(gameState)

	colisionList = pygame.sprite.spritecollide(avatar, enemies,False)
	if avatar.blink == False:
		for enemy in colisionList:
			enemy.randomTopPosition()
			enemy.randomSpeed()
			#enemies.add(enemy)
			#allSprites.add(enemy)
			avatar.startBlink()
			gameState.lives -=1

	allSprites.draw(screen) #draws all sprites
	leftarrow.draw(screen,milliseconds,gameState)
	rightarrow.draw(screen,milliseconds,gameState)
	scoreboard.draw(screen,gameState)
	pygame.display.flip()