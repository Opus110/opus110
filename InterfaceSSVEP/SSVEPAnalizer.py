 # -*- coding: utf-8 -*-
from emokit.emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent
import threading
import logging
from time import sleep
from numpy import sin, arange, pi, sqrt
from scipy.signal import lfilter, firwin, periodogram
from pylab import figure, plot, grid, show

key = threading.Lock()


logging.basicConfig( level=logging.DEBUG,format="[%(levelname)s] – %(threadName) -10s : %(message)s")

class SSVEPAnalizer(object):
	sensorList = 'O1 O2'
	packages = []
	emotivThread = None
	analizerThread = None
	bufferlength = 128*3
	epocBufferState = False
	analizerState = False
	AnalizerResult = None
	def __init__(self,sensors=None):
		self.emotivThread =  threading.Thread(target=self.epocBuffer, name="Epoc Buffer")
		self.analizerThread = threading.Thread(target=self.Analizer,name="Epoc Analizer")
		if sensors!=None:
			self.sensorList = sensors
		pass
	def Analizer(self):
		cont = 0	
		Test = False		
		while self.analizerState:
			self.AnalizerResult = self.analize()
			sleep(10)
			
		pass
		logging.debug("Saliendo del analizador")
		self.stopBuffer()			
		pass
	def startAnalizer(self):
		if self.analizerState == False:
			self.startBuffer()
			sleep(3)
			logging.debug("Iniciando analizador")
			self.analizerState = True
			self.analizerThread.start()
		pass
	def stopAnalizer(self):
		logging.debug("Deteniendo analizador")
		self.analizerState = False
		pass
	def analize(self):
		#logging.debug("Analize")
		nSamples = self.bufferlength
		sampleRate = 128. #this is the epoc rate
		t = arange(nSamples) / sampleRate
		cutoff_hz = 60
		nyq_rate = sampleRate / 2.
		numtaps = 29
		fir_coeff = firwin(numtaps, cutoff_hz/nyq_rate)
		signals = {}
		results = {}
		#sensors = 'AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4'.split(' ')
		sensors = self.sensorList.split(' ')
		key.acquire()
		for name in sensors:
			signals[name] = []
			pass
		for packet in self.packages[:self.bufferlength]:
			for name in sensors:
				signals[name].append(packet.sensors[name]['value'])
				#if name == 'O2':
				#	print packet.sensors[name]
				pass
			pass
		for name in sensors:
			#print signals[name]
			filtered_signal = lfilter(fir_coeff, 1.0, signals[name])
			warmup = numtaps - 1
 
			# The phase delay of the filtered signal
			delay = (warmup / 2) / sampleRate
			#print(len(signals[name]))
			#print "\n"
			#print signals[name]
			fres, espect = periodogram(signals[name], sampleRate)
			fmax, amax = self.fundamentalFrequency(fres,espect)
			#logging.debug(name+" Max frecuency: "+str(fmax))
			#logging.debug(name+" Max espectrum: "+str(amax))
			results[name] = (fmax,amax)
			if False:
				figure(1)
				plot(t,signals[name])
				plot(t-delay,filtered_signal,'r')
				plot(t[warmup:]-delay, filtered_signal[warmup:], 'g', linewidth=4)
				grid(True)

				figure(2)
				plot(fres, espect)


				show()
				pass

			pass
		#print results
		key.release()
		return results			
		pass
	def fundamentalFrequency(self,f,espect):
		fmax = 0
		amax = 0
		for i in range(len(espect)):
			if espect[i]> amax :
				amax = espect[i]
				fmax = f[i]
			pass
		return fmax,amax
		pass
	def stopBuffer(self):
		logging.debug("Deteniendo Buffer")
		self.epocBufferState =  False
		pass
	def startBuffer(self):
		if self.epocBufferState == False:
			self.epocBufferState = True
			self.emotivThread.start()	
			while len(self.packages) < self.bufferlength and self.epocBufferState:
				logging.debug("Waiting an apropiate buffer ("+str(self.bufferlength)+" packages), actual "+str(len(self.packages)))
				sleep(1)
				pass
		pass
	def epocBuffer(self):
		cont=0
		logging.debug("Iniciando buffer del epoc")
		headset = Emotiv(display_output = False)
		gevent.spawn(headset.setup)
		gevent.sleep(0) 

		showFillMessage = True
		while self.epocBufferState:
			packet = headset.dequeue()
			key.acquire()
			if packet == None:
			    logging.debug("Error, paquete nulo")
			else:
			    #print packet.gyro_x, packet.gyro_y
				self.packages.append(packet)
				#print packet.sensors['O2']['value']
			
			if len(self.packages) > self.bufferlength :
				if showFillMessage:
					logging.debug("Buffer lleno con "+str(self.bufferlength)+" paquetes")
					showFillMessage ^=True
				self.packages = self.packages[10:]
			gevent.sleep(0)
			key.release()
			pass
		headset.close()
		logging.debug("Buffer detenido")
		pass
	pass


if __name__ == "__main__":
	analizer =  SSVEPAnalizer('O1 O2')
	try:
		analizer.startBuffer()
		sleep(10)
		while True:
			#print analizer.AnalizerResult["O1"][0],analizer.AnalizerResult["O2"][0], analizer.AnalizerResult["AF3"][0]
			result = analizer.analize()
			print result
			sleep(1)

			pass
		pass
	except KeyboardInterrupt, e:
		analizer.stopBuffer()
		logging.debug("Exit")			
		pass
	pass