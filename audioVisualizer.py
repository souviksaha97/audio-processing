import numpy as np
import pyaudio
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn')



SAMPLESIZE = 4096 # number of data points to read at a time
SAMPLERATE = 44100 # time resolution of the recording device (Hz)

p = pyaudio.PyAudio() # instantiate PyAudio

stream=p.open(format=pyaudio.paInt16,channels=1,rate=SAMPLERATE,input=True,
              frames_per_buffer=SAMPLESIZE) # use default input device to open audio stream


fig = plt.figure()
ax = plt.axes(xlim=(0, SAMPLESIZE-1), ylim=(-9999, 9999))
line, =ax.plot([], [], lw = 0.5)


def init():
	line.set_data([],[])
	return line,

def animate(i):
	x = np.linspace(0, SAMPLESIZE-1, SAMPLESIZE)
	y = np.frombuffer(stream.read(SAMPLESIZE), dtype=np.int16)
	line.set_data(x, y)
	return line,

anim = FuncAnimation(fig, animate, init_func=init, frames=30,
					interval= 20, blit=True)


plt.show()

# stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()