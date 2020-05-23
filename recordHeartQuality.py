from scipy import signal
import numpy as np
import pyaudio
import wave
import matplotlib.pyplot as plt
from scipy.fftpack import fft


SAMPLESIZE = 4096 # number of data points to read at a time
SAMPLERATE = 8000 # time resolution of the recording device (Hz)

RECORD_LENGTH = 20
FORMAT = pyaudio.paInt16

filename = "recorded.wav"

p = pyaudio.PyAudio() # instantiate PyAudio

stream=p.open(format=FORMAT,channels=1,rate=SAMPLERATE,input=True,
              frames_per_buffer=SAMPLESIZE) # use default input device to open audio stream
y = []

print("Start")

for i in range(int(SAMPLERATE / SAMPLESIZE * RECORD_LENGTH)):
	data = stream.read(SAMPLESIZE)
	frame = np.frombuffer(data, dtype=np.int16).tolist()
	print(len(frame))
	y.extend(frame)

print("End")

stream.stop_stream()
stream.close()

p.terminate()
# # save audio file
# # open the file in 'write bytes' mode
# wf = wave.open(filename, "wb")
# # set the channels
# wf.setnchannels(1)
# # set the sample format
# wf.setsampwidth(p.get_sample_size(FORMAT))
# # set the sample rate
# wf.setframerate(SAMPLERATE)
# # write the frames as bytes
# wf.writeframes(b''.join(frames))
# # close the file
# wf.close()
# print(len(y))
# x = range(len(y))
# plt.plot(x,y)
# plt.show()
# f, Pxx_den = signal.periodogram(y, SAMPLERATE)
# plt.semilogy(f, Pxx_den)
yf = 20*np.log10((((np.abs(fft(y))))[:int(SAMPLERATE/2)])/11490308)
plt.xscale('log')
# plt.yscale('log')

plt.plot(yf)
plt.show()
print(max(yf))