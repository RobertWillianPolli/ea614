import math
import numpy as np
import matplotlib.pyplot as plt

def kaiser(wp, wr):
    wc = (wp + wr) / 2
    d = 0.01
    Ap = 20 * math.log10((1 + d) / (1 - d))
    Ar = -20 * math.log10(d)

    if Ar < 21:
        b = 0
        D = .9222

    elif Ar < 50:
        b = 0.5842 * (Ar - 21) ** 0.4 + 0.07886 * (Ar - 21)
        D = (Ar - 7.95) / 14.36
    else:
        b = .1102 * (Ar - 8.7)
        D = (Ar - 7.95) / 14.36

    k = math.ceil(math.pi * D / (wr - wp) - .5)
    M = 2 * k + 1

    n = np.arange(-k, k + 1, 1)

    w = np.i0(b * np.sqrt(1 - (4 / M ** 2) * n ** 2))
    w = np.divide(w, np.i0(b))

    h = wc / math.pi * np.sinc(wc * n / math.pi) * w

    return h

def espectro(y, fp, fr):
    # modulo da transf. de Fourier
    Y = np.abs(np.fft.fft(y))
    # frequencias avaliadas
    w = np.linspace(0, 2 * math.pi, len(Y))

    # exibe o grafico do espectro
    plt.figure()
    plt.plot(w, Y / np.max(Y))

    plt.title(f"Espectro de frequências - $\Omega_P$ = {fp} e $\Omega_R$ = {fr}")
    plt.xlabel('$\Omega$ [rad]', fontsize=10)
    plt.ylabel('|$Y(e^{j\Omega})$|', fontsize=10)

    plt.grid(True)
    plt.xlim((0, 2 * math.pi))

    plt.show()

    return Y, w


if __name__ == "__Main__":
    freq = [[0.45, 2], [0.45, 0.5], [1.5, 2]]
    H = []
    Omega = [[],[],[]]

    for f in freq:
        H.append(espectro(kaiser(f[0], f[1]), f[0], f[1]))