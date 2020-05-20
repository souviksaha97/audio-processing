import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from scipy.fftpack import fft
plt.style.use('seaborn')

SAMPLESIZE = 4096 # number of data points to read at a time
SAMPLERATE = 44100 # time resolution of the recording device (Hz)
NO_BARS = 24
p = pyaudio.PyAudio() # instantiate PyAudio
stream=p.open(format=pyaudio.paInt16,channels=1,rate=SAMPLERATE,input=True,
              frames_per_buffer=SAMPLESIZE) # use default input device to open audio stream

# set up plotting
x = range(0, NO_BARS)
for i in range(10):
	# y = np.frombuffer(stream.read(SAMPLESIZE), dtype=np.int16)

	y = np.frombuffer(stream.read(SAMPLESIZE), dtype=np.int16)
	yf = ((np.abs(fft(y))/20)[:2048])
	xf = np.linspace(0, SAMPLERATE/2-1, SAMPLESIZE/2)
	xsplit = np.linspace(0, SAMPLERATE/4-1, NO_BARS, dtype=int)
	ysplit_index = np.linspace(0, SAMPLESIZE/4-1, NO_BARS, dtype=int)
	yfsplit = (yf[ysplit_index])

print(xsplit, yfsplit, x)
plt.bar(x=x, height=yfsplit)
plt.show()
	# xf = np.linspace(0, SAMPLERATE/2-1, SAMPLESIZE/2)
# plt.magnitude_spectrum(y, Fs=SAMPLERATE)
# 	plt.bar(xsplit, yfsplit)
# 	plt.show()
# 	plt.close()
# print(y)