import math
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

""" Rotina que exibe o espectro de magnitude (X(ejw)) de um sinal discreto """

def espectro(y, fs):
    # modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    # frequencias avaliadas
    w = np.linspace(0, 2 * math.pi, len(Y))

    f = w * fs

    # exibe o grafico do espectro
    plt.figure()
    #plt.plot(w, Y / np.max(Y))
    plt.plot(f, Y / np.max(Y))

    plt.title("Espectro de frequências")
    #plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.xlabel('Frequência [Hz]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)

    plt.grid(True)
    #plt.xlim((0, 2 * math.pi))
    
    plt.show()

    return Y, w

# Fs -  Taxa de amostragem

Fs, y = wavfile.read("creed_overcome.wav")

y=(y[:,0]+y[:,1])/2
espectro(y, Fs)

