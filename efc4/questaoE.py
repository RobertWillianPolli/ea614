import numpy as np
from scipy.io import wavfile
from questaoD import kaiser
import matplotlib.pyplot as plt

def espectro(y):
    # modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    # frequencias avaliadas
    w = np.linspace(0, 2 * np.pi, len(Y))

    return(Y, w)

Fs, y = wavfile.read("creed_overcome.wav")

y=(y[:,0]+y[:,1])/2

Hjw = kaiser(0.45, 0.5)

filtrado, w = espectro(np.convolve(y, Hjw))

plt.figure()
plt.plot(w, filtrado/np.max(filtrado))

plt.title("Sinal filtrado")
plt.xlabel('$\Omega$ [rad]', fontsize=10)
plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)

plt.grid(True)
plt.show()