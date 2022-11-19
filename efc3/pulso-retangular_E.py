import matplotlib.pyplot as plt
from scipy import signal, integrate
import numpy as np

from butterworth import Hb
from chebyshev_A import Hc

def Hideal(jw):
    if abs(jw) <= wc:
        return(1)
    else:
        return(0)

wc = 10
e = 0.9
n_B = 2
n_C = 3

wm = 5
tal = (2*np.pi)/wm
j= complex(0,1)

w = np.linspace(-50,50,200)
gain = [[], [], []]
Xjw = []
Xt = []

Yb = []
Yc = []
Yideal = []

for omega in w:
    gain[0].append(Hideal(omega))
    gain[1].append(Hb(omega, n_B, wc))
    gain[2].append(Hc(omega, n_C, wc, e))

    x_e = lambda t: signal.square(5 * t / 2 + (np.pi / 2)) * np.exp(-j * omega * t)
    Xjw.append(abs(integrate.quad(x_e, -tal / 2, tal / 2)[0]))

for index in range(len(Xjw)):
    Yideal.append(Xjw[index] * gain[0][index])
    Yb.append(Xjw[index] * gain[1][index])
    Yc.append(Xjw[index] * gain[2][index])

#=====================================================

plt.figure(1)
stemlines = plt.stem(w, np.array(Xjw), "b", use_line_collection=True)
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("|X(jw)|")
plt.title("Sinal de entrada dos filtros")

plt.show()

#=====================================================

'''plt.figure(1)
stemlines = plt.stem(w, np.array(gain[0]), "b", use_line_collection=True, label="|Hideal(jw)|")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(w, np.array(gain[1]), "r", use_line_collection=True, label="|Hc(jw)|")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(w, np.array(gain[2]), "g", use_line_collection=True, label="|Hb(jw)|")
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("Módulo da resposta em frequência")
plt.title("Comparação das respostas em frequência")

plt.legend()
plt.show()

#=====================================================

plt.figure(1)
stemlines = plt.stem(w, np.array(Yideal), "b", use_line_collection=True, label="Filtro ideal")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(w, np.array(Yb), "r", use_line_collection=True, label="Filtro Butterworth")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(w, np.array(Yc), "g", use_line_collection=True, label="Filtro Chebyshev")
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("Módulo da saída")
plt.title("Comparação das saídas dos filtros")

plt.legend()
plt.show()

#====================================================='''
