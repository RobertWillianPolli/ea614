from scipy.io import wavfile
from questao-D import kaiser

Fs, y = wavfile.read("creed_overcome.wav")

y=(y[:,0]+y[:,1])/2

Hjw = kaiser(0.45, 0.5)

print(len(Hjw))