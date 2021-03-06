# This is an example of popping a packet from the Emotiv class's packet queue
# and printing the gyro x and y values to the console. 

from emokit.emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent

if __name__ == "__main__":
    headset = Emotiv(display_output = False)
    gevent.spawn(headset.setup)
    gevent.sleep(0) 
    try:
        while True:
            packet = headset.dequeue()
            if packet == None:
                print "Error, paquete nulo"
            else:
                print packet.gyro_x, packet.gyro_y
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()
