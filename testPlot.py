from numpy import sin, arange, pi, sqrt
from scipy.signal import lfilter, firwin, periodogram
from pylab import figure, plot, grid, show


nSamples = 128
sampleRate = 128.
t = arange(nSamples) / sampleRate


f1= 4.0 #Hz
A1 = 10.0

f2 = 50 #Hz
A2 = 3.0

ftest = 1 #Hz
Atest = 3.0


signala = A1 * sin(2*pi*f1*t) +  A2*sin(2*pi*f2*t)
#signalb =  Atest*sin(2*pi*ftest*t)

nyq_rate = sampleRate / 2.
cutoff_hz = 40
numtaps = 29
fir_coeff = firwin(numtaps, cutoff_hz/nyq_rate)
filtered_signal = lfilter(fir_coeff, 1.0, signala)

# The first N-1 samples are "corrupted" by the initial conditions
warmup = numtaps - 1
 
# The phase delay of the filtered signal
delay = (warmup / 2) / sampleRate
 
fres, espect = periodogram(filtered_signal, sampleRate)


figure(1)
plot(t,signala)
#plot(t,signalb)
plot(t-delay,filtered_signal,'r')
plot(t[warmup:]-delay, filtered_signal[warmup:], 'g', linewidth=4)
grid(True)

figure(2)
plot(fres, espect)


show()

