import math
import numpy as np
import IPython.display as ipd
from scipy.io import wavfile
import matplotlib.pyplot as plt

def decimacao(y):
    yDec = []
    for position, value in enumerate(y):
        if not(position % 6):
            yDec.append(value)
    return(yDec)

# Fs -  Taxa de amostragem

Fs, y = wavfile.read("creed_overcome.wav")

y=(y[:,0]+y[:,1])/2

#ipd.Audio(data=y,rate=Fs, autoplay=True)
ipd.Audio(data=decimacao(y),rate=Fs/6, autoplay=True)