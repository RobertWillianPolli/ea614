import numpy as np
import matplotlib.pyplot as plt

with open("./EEG.txt", "r") as f:
    eeg = [float(lines) for lines in f.read().splitlines()]

#time = np.linspace(0,len(eeg)/250, len(eeg))

freq = np.linspace(0,125,len(eeg))

Y = abs(np.fft.fft(np.array(eeg)))
print(len(Y))
print("Índice 'k' do maior módulo:", Y[:int(len(Y)/2)].argmax())
print("Valor da transformada nesse ponto:", Y[:int(len(Y)/2)].max())
print("Frequência associada ao índice:", freq[Y[:int(len(Y)/2)].argmax()])

plt.figure()

#plt.plot(time, eeg)
plt.plot(freq, Y)

#plt.title("Eletrocardiograma")
plt.title("Espectro de magnitude do EEG")

plt.xlabel("Frequência (Hz)", fontsize=10)
#plt.xlabel("Tempo (s)", fontsize=10)

plt.ylabel("|$Y(e^{j\Omega})$|", fontsize=10)
#plt.ylabel("EEG", fontsize=10)

plt.grid(True)
plt.show()