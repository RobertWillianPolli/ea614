import matplotlib.pyplot as plt
from scipy import signal, integrate
import numpy as np

global tal
wm = 5
tal = (2*np.pi)/wm
j= complex(0,1)

w = np.linspace(0,40,100)
Xjw = []

for omega in w:
    x_e = lambda t: signal.square(5 * t / 2 + (np.pi / 2)) * np.exp(-j * omega * t)
    Xjw.append(abs(integrate.quad(x_e, -tal/2, tal/2)[0]))

stemlines = plt.stem(w, np.array(Xjw), use_line_collection=True)
plt.setp(stemlines, 'linestyle', 'dotted')

plt.xlabel("Frequência angular (rad/s)")
plt.ylabel("|Hc(jw)|")
plt.title("Filtro de Chebyshev - wc = 10 rad/s, n = 3")

plt.show()