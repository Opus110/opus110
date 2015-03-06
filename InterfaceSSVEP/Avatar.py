import pygame
from Assets import assets
from GameState import *
from Analizer import *
import gevent

debug = False;

class Avatar(pygame.sprite.DirtySprite):
	def __init__(self,width, height):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.image = assets["avatar"]
		self.image = pygame.transform.scale(self.image,(50,50))
		self.rect = self.image.get_rect()
		self.rect.y = self.height - self.rect.h - 100
		self.rect.x = (self.width - self.rect.w)/2
		self.blink = False
		self.blinkCount = 0
		self.blinkState = 0
		self.allSprites = None
		self.enemies = None
		self.leftFrec = 8 
		self.rightFrec = 12
		self.analizer = Analizer([self.leftFrec,self.rightFrec])
		self.useAnalizer = True
		pass
	def startBlink(self):
		if self.blink == False:
			self.blinkCount =0
			self.blink =True
		pass
	def calculateBlink(self):
		if self.blink :
				self.blinkCount += 1
				if self.blinkCount % 10 == 0:
					self.blinkState = 1 if self.blinkState ==2 else 2
					if self.blinkState == 1:
						self.allSprites.add(self)
					else:
						self.allSprites.remove(self)
				if self.blinkCount > 300:
					self.blink = False
					self.blinkState = 1
					self.allSprites.add(self)
		pass
	def update(self,*args):
		gameState = args[0]
		if gameState.state == PLAYING:
			hspeed = 3
			speed=[hspeed,0]

			mouse =  pygame.mouse.get_pressed()
			if debug:
				print "Pressed buttons :",mouse
			
			if self.analizer.signal != None:
				print self.analizer.signal['MaxO1'],self.analizer.signal['MaxO2']
				pass
			if(self.useAnalizer):
				if self.analizer == None:
					print "Analizer is null"
				elif self.analizer.signal != None:
					max1 =  self.analizer.signal["MaxO1"]
					max2 =  self.analizer.signal["MaxO2"]
					avg =  (max1+max2)/2
					print max1,max2,avg
					if avg >= 9 and avg <= 11: #move left
						speed[0] = -hspeed
						print "Move left"
						pass
					elif avg>11 and avg <=13: #move right
						speed[0] = hspeed
						print "Move right"
						pass
					else:
						speed[0]  = 0
					pass
				pass			
			if (mouse[0] == 1 and mouse[2] == 1) == False:
				if mouse[0] == 1:
					speed[0] = -hspeed
				elif mouse[2] == 1:
					speed[0] = hspeed
				elif self.analizer == None:
					speed[0] = 0
			else:
				speed[0]=0
			gevent.sleep(0)
			self.rect = self.rect.move(speed)
			if(self.rect.x < 0):
				self.rect.x = 0
			if(self.rect.x > self.width-self.rect.w ):
				self.rect.x = self.width-self.rect.w
			self.calculateBlink()
		pass
