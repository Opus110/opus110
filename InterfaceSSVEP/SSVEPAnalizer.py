 # -*- coding: utf-8 -*-
from emokit.emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent
import threading
import logging
from time import sleep


logging.basicConfig( level=logging.DEBUG,format="[%(levelname)s] – %(threadName) -10s : %(message)s")

class SSVEPAnalizer(object):
	packages = []
	emotivThread = None
	bufferlength = 128
	epocBufferState = False
	analizerState = False
	def __init__(self):
		self.emotivThread =  threading.Thread(target=self.epocBuffer,
			args=[self.packages,self.bufferlength], name="Epoc Buffer")
		pass
	def startAnalizer(self):
		try:
			cont = 0
			self.startBuffer()
			while cont < 1000:
				logging.debug(cont)
				logging.debug("Packages length: "+str(len(self.packages)))
				cont+= 1
				pass
			pass
		except KeyboardInterrupt, e:
			#self.stopBuffer()
			logging.debug("Saliendo del analizador")
			pass
		finally:
			self.stopBuffer()
			pass
			
		pass
	def analize(self):

		pass

	def stopBuffer(self):
		logging.debug("Deteniendo Buffer")
		self.epocBufferState =  False
		pass
	def startBuffer(self):
		if self.epocBufferState == False:
			self.epocBufferState = True
			self.emotivThread.start()	
		while len(self.packages) < self.bufferlength:
			logging.debug("Waiting an apropiate buffer ("+str(self.bufferlength)+" packages), actual "+str(len(self.packages)))
			sleep(1)
			pass
		pass
	def epocBuffer(self,packages,bufferlength):
		cont=0
		logging.debug("Iniciando buffer del epoc")
		showFillMessage = True
		packages.append(cont)
		while self.epocBufferState:
			cont+=1
			packages.append(cont)
			if len(packages) > bufferlength :
				if showFillMessage:
					logging.debug("Buffer lleno con "+str(bufferlength)+" paquetes")
					showFillMessage ^=True
				packages.pop()
			pass
		logging.debug("Buffer detenido")
		pass
	pass


if __name__ == "__main__":
	analizer =  SSVEPAnalizer()
	analizer.startAnalizer()
	pass