from emokit import emotiv
import platform
if platform.system() == "Windows":
    import socket
import gevent

if __name__ == "__main__":
  headset = emotiv.Emotiv()    
  gevent.spawn(headset.setup)
  gevent.sleep(1000)
  
  try:
    while True:
      raw_input()
      packet = headset.dequeue()
      print packet.gyro_x, packet.gyro_y
      gevent.sleep(0)
  except KeyboardInterrupt:
    headset.close()
  finally:
    headset.close()