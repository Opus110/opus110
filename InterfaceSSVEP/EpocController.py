 # -*- coding: utf-8 -*-
import threading
import logging
from time import sleep


threads = list()
logging.basicConfig( level=logging.DEBUG,format="[%(levelname)s] â?? %(threadName) -10s : %(message)s")


def startController():
	global runEpoc
	runEpoc =  True
	#headset = Emotiv(display_output = False)
	#headset.setup()
	while runEpoc:
	    #packet = headset.dequeue()
        #if packet == None:
        #    print "Error, paquete nulo"
        #else:
        #    print packet.gyro_x, packet.gyro_y
		gevent.sleep(0)
    #headset.close()
	logging.debug("Exit controller")
	pass
		
def stopController():
	global runEpoc
	runEpoc = False
	pass





if __name__ == "__main__":
	t1 = threading.Thread(target=startController,name='Start EpocController')
	t2 = threading.Thread(target=stopController,name='Stop EpocController')

	threads.append(t1)
	threads.append(t2)
	t1.start()
	sleep(10)
	t2.start()


	pass
