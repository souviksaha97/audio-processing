import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import scipy
from scipy.fftpack import fft
plt.style.use('seaborn')



SAMPLESIZE = 4096 # number of data points to read at a time
SAMPLERATE = 44100 # time resolution of the recording device (Hz)

p = pyaudio.PyAudio() # instantiate PyAudio

stream=p.open(format=pyaudio.paInt16,channels=1,rate=SAMPLERATE,input=True,
              frames_per_buffer=SAMPLESIZE) # use default input device to open audio stream


fig = plt.figure()
ax = plt.axes(xlim=(0, SAMPLERATE/2), ylim=(0, 500))
line, =ax.plot([], [], lw = 0.5)


def init():
	line.set_data([],[])
	return line,

def animate(i):
	y = np.frombuffer(stream.read(SAMPLESIZE), dtype=np.int16)
	yf = ((np.abs(fft(y))/4096))[:int(SAMPLESIZE/2)]
	xf = np.linspace(0, SAMPLERATE/2-1, SAMPLESIZE/2)
	line.set_data(xf, yf)
	return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=200,
					interval= 20, blit=True)


plt.show()

# stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()