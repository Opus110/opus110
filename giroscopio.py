
from emokit import emotiv
import platform
if platform.system() == "Windows":
    import socket
import gevent

if __name__ == "__main__":
  headset = emotiv.Emotiv(display_output=True)    
  gevent.spawn(headset.setup)
  gevent.sleep(0)
  try:
    while True:
      packet = headset.dequeue()
      print packet.gyro_x, packet.gyro_y
      print packet.raw_data
      gevent.sleep(0)
  except KeyboardInterrupt:
    headset.close()
  finally:
    headset.close()

