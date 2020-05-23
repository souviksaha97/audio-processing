import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy
from scipy.fftpack import fft
plt.style.use('seaborn')



SAMPLESIZE = 1024 # number of data points to read at a time
SAMPLERATE = 16000 # time resolution of the recording device (Hz)
NO_BARS=10
p = pyaudio.PyAudio() # instantiate PyAudio

stream=p.open(format=pyaudio.paInt16,channels=1,rate=SAMPLERATE,input=True,
              frames_per_buffer=SAMPLESIZE) # use default input device to open audio stream

x = range(0, NO_BARS)
fig = plt.figure()
ax = plt.axes(xlim=(0, NO_BARS-1), ylim=(0, 1000))
# ax = plt.axes(xlim=(1, SAMPLERATE/2), ylim=(0, 1000))
line, =ax.plot([], [], lw = 0.5)


def init():
	line.set_data([],[])
	return line,

def animate(i):
	y = np.frombuffer(stream.read(SAMPLESIZE), dtype=np.int16)
	yf = ((np.abs(fft(y))/200))[:int(SAMPLESIZE/2)]
	# xf = np.linspace(0, SAMPLERATE/2-1, SAMPLESIZE/2)
	xsplit = np.linspace(0, SAMPLERATE/2-1, NO_BARS, dtype=int)
	ysplit_index = np.linspace(0, SAMPLESIZE/2-1, NO_BARS, dtype=int)
	yfsplit = (yf[ysplit_index])
	# line.set_data(xf, yf)
	line.set_data(x, yfsplit)
	# print(yfsplit)
	return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=10,
					interval= 20, blit=True)


plt.show()

# stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()