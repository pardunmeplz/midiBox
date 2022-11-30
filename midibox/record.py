import wave
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import typing

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

record = pyaudio.PyAudio()

stream = record.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("starting recording")
second = 1
frames:typing.List = []

for _ in range(0,int(RATE/FRAMES_PER_BUFFER*second)):
    data = stream.read(FRAMES_PER_BUFFER)
    frames.append(data)

stream.start_stream()
stream.close()
record.terminate()


with wave.open("audio/output.wav","wb") as audio:
    audio.setnchannels(CHANNELS)
    audio.setsampwidth(record.get_sample_size(FORMAT))
    audio.setframerate(RATE)
    audio.writeframes(b"".join(frames))