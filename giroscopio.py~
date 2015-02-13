<<<<<<< HEAD:emotivTest.py
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
=======
from emokit import emotiv
import platform
if platform.system() == "Windows":
    import socket
import gevent

if __name__ == "__main__":
  headset = emotiv.Emotiv(display_output=False)    
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
>>>>>>> 6b91e2380abdb7ff639a6653077ab6fef9d61a24:giroscopio.py
