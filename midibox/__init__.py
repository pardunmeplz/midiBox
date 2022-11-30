import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load('audio/pfft.wav')
plt.plot(y)
plt.show()