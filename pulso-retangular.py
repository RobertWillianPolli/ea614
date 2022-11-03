import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

global tal

wm = 5

tal = (2*np.pi)/wm

t = np.linspace(-tal, tal, 100)

x = signal.square(5*t/2+(np.pi/2))

plt.ylabel("Amplitude")
plt.xlabel("Tempo (s)")
plt.plot(t, x)
plt.show()

fft = np.fft.fft(x)
T = t[1] - t[0] # 0.001 -> 1/T = 1000
N = x.size
f = np.fft.fftfreq(len(x), T)
frequencias = f[:N // 2]
amplitudes = np.abs(fft)[:N // 2] * 1 / N

plt.ylabel("Amplitude")
plt.xlabel("Frequência (Hz)")
plt.bar(frequencias, amplitudes, width=1.5)
plt.show()'''