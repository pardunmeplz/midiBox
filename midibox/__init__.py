import wave
import matplotlib.pyplot as plt
import numpy as np


with wave.open("audio/pfft.wav",'rb') as audio:
    samplQ = audio.getframerate()
    nSamples = audio.getnframes()
    signal = audio.readframes(-1)

time = nSamples/samplQ
signalArray = np.frombuffer(signal,dtype=np.int16)
times = np.linspace(0,time,num=nSamples*2)

plt.plot(times,signalArray)
plt.show()