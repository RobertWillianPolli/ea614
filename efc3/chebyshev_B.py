import numpy as np
import matplotlib.pyplot as plt
from math import cos, cosh, acos, acosh

# Definição das contantes

global wc, n

wc = 10           # frequência de corte, em rad/s
n = 3

n_plot = [[], [], [], [], []]

def Hc(jw, e):
    return((1+(e**2)*(Tn(abs(jw)/wc)**2))**-0.5)

def Tn(rate):
    if rate <= 1:
        value = cos(n*acos(rate))
    else:
        value = cosh(n*acosh(rate))
    return(value)

for index, e in enumerate([0.1, 0.3, 0.5, 0.7, 0.9]):
    for w in range(-100, 100):
        n_plot[index].append(Hc(w, e))

plt.figure(1)
stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[0]), "b", use_line_collection=True, label="e = 0.1")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[1]), "r", use_line_collection=True, label="e = 0.3")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[2]), "g", use_line_collection=True, label="e = 0.5")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[3]), "c", use_line_collection=True, label="e = 0.7")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[4]), "y", use_line_collection=True, label="e = 0.9")
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("|Hc(jw)|")
plt.title("Filtro de Chebyshev - wc = 10 rad/s, n = 3")

plt.legend()
plt.show()