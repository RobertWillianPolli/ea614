import numpy as np
import matplotlib.pyplot as plt

global wc
wc = 10

n_plot = [[], [], [], [], []]

def Hb(jw, n):
    return((1+(jw/wc)**(2*n))**(-0.5))

for N in [1, 2, 3, 4, 5]:
    for w in range(-100,100):
        n_plot[N-1].append(Hb(w, N))

plt.figure(1)
stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[0]), "b", use_line_collection=True, label="Ordem: 1")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[1]), "r", use_line_collection=True, label="Ordem: 2")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[2]), "g", use_line_collection=True, label="Ordem: 3")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[3]), "c", use_line_collection=True, label="Ordem: 4")
plt.setp(stemlines, 'linestyle', 'dotted')

stemlines = plt.stem(np.array(range(-100,100)), np.array(n_plot[4]), "y", use_line_collection=True, label="Ordem: 5")
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("|Hb(jw)|")
plt.title("Filtro de Butterworth - wc = 10 rad/s")

plt.legend()
plt.show()



