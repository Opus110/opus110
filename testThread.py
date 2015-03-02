# -*- coding: utf-8 -*-
import threading
from time import sleep
import logging



#Thread test
def func1():
	cont = 100
	while True and cont>0 :
		logging.debug("Some work of the first function")
		sleep(2)
		cont -=1
		pass
	pass

def func2():
	cont = 100
	while True and cont > 0:
		logging.debug("Some work of the second function")
		sleep(3)
		cont -= 1
		pass
	pass



if __name__ == "__main__":
	logging.basicConfig( level=logging.DEBUG,format="[%(levelname)s] – %(threadName) -10s : %(message)s")
	threads = list()
	t1 = threading.Thread(target=func1)
	t2 = threading.Thread(target=func2)
	threads.append(t1)
	threads.append(t2)
	for t in threads:
		t.start()
		pass
	pass