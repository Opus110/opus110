import pygame

debug = True

STARTED = 0
PLAYING = 1
PAUSED = 2
ENDED = 3



class GameState():
	running = True
	score = 0
	counter = 0
	level = 1
	lives = 3
	distance = 0
	state = PLAYING
	def __init__(self):
		self.resetGame()
		pass
	def resetGame(self):
		self.score = 95
		self.level = 1
		self.running = True
		self.state = PLAYING
		self.counter = 0
		self.distance = 0
		pass
	def update(self):
		if(self.state == PLAYING):
			self.counter +=1
			self.score += 1 if self.counter%100 == 0 else 0
			self.distance += 1 if self.counter%10 == 0 else 0
			if self.score%100 == 0 and self.score > 0:
				self.level = self.score/100 + 1
		self.printDebug()
		pass
	def addPoints(self, points):
		self.score += points
		pass
	def pause(self):
		self.state =  PAUSED
	def resume(self):
		self.state = PLAYING
	def togglePause(self):
		if self.state == PAUSED:
			self.resume()
		elif self.state == PLAYING:
			self.pause()
	def  printDebug(self):
		if debug:
			print "Score: ",self.score
			print "Level: ", self.level
			print "Lives: ", self.lives
			print "State: ", self.state
		pass
	pass