# This is an example of popping a packet from the Emotiv class's packet queue
# and printing the gyro x and y values to the console. 

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



def fundamentalFrequency(f,espect):
    fmax = 0
    amax = 0
    for i in range(len(espect)):
        if espect[i]> amax :
            amax = espect[i]
            fmax = f[i]
        pass
    return fmax,amax
    pass

def analize(signals,sensors,bufferlength):
        #logging.debug("Analize")
        nSamples = bufferlength
        sampleRate = 128. #this is the epoc rate
        t = arange(nSamples) / sampleRate
        cutoff_hz = 60
        nyq_rate = sampleRate / 2.
        numtaps = 29
        fir_coeff = firwin(numtaps, cutoff_hz/nyq_rate)
        results = {}
        #sensors = 'AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4'.split(' ')      
        for name in sensors:
            #print signals[name]
            filtered_signal = lfilter(fir_coeff, 1.0, signals[name])
            warmup = numtaps - 1
            #print filtered_signal
            # The phase delay of the filtered signal
            delay = (warmup / 2) / sampleRate
            #print(len(signals[name]))
            #print "\n"
           
            fres, espect = periodogram(signals[name], sampleRate)
            fmax, amax = fundamentalFrequency(fres,espect)
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
        
        print results
        return results          
        pass


if __name__ == "__main__":
    headset = Emotiv(display_output = False)
    gevent.spawn(headset.setup)
    gevent.sleep(0)
    packets = {};
    bufferLenght = 256
    sensors = "AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4".split(' ')
    for name in sensors:
        packets[name] = []
        pass
    try:
        while True:
            p = headset.dequeue()
            if p != None:
                for name in sensors:
                    packets[name].append(p.sensors[name]['value'])
                    pass
               
                if len(packets[sensors[0]]) >= bufferLenght:
                    print 'analize '
                    signal = analize(packets,sensors,bufferLenght)
                    for name in sensors:
                        packets[name] = []
                        pass
                    pass
            gevent.sleep(0)
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()
    print "Exit!!!"
