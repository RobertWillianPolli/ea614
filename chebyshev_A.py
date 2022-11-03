import numpy as np
import matplotlib.pyplot as plt
from math import cos, cosh, acos, acosh

# Definição das contantes

global wc, e

wc = 10           # frequência de corte, em rad/s
e = 0.2
n_plot = [[], [], [], [], []]

def Hc(jw, n):
    return((1+(e**2)*(Tn(abs(jw)/wc, n)**2))**-0.5)

def Tn(rate, n):
    if rate <= 1:
        value = cos(n*acos(rate))
    else:
        value = cosh(n*acosh(rate))
    return(value)

for N in [1, 2, 3, 4, 5]:
    for w in range(-100, 100):
        n_plot[N-1].append(Hc(w, N))

plt.figure(1)
stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[0]), "b", use_line_collection=True, label="Ordem 1")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[1]), "r", use_line_collection=True, label="Ordem 2")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[2]), "g", use_line_collection=True, label="Ordem 3")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[3]), "c", use_line_collection=True, label="Ordem 4")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[4]), "y", use_line_collection=True, label="Ordem 5")
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("|Hc(jw)|")
plt.title("Filtro de Chebyshev - wc = 10 rad/s, e = 0.2")

plt.legend()
plt.show()