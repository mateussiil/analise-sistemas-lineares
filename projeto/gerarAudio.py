import pyaudio
import wave, struct, math 
import matplotlib.pyplot as plt
import numpy as np
import random

sr = 22050 
T = 15.0    
t = np.linspace(0, T, int(T*sr), endpoint=False) 

notas = [0.5*np.sin(2*np.pi*220*t), 0.5*np.sin(2*np.pi*440*t), 0.5*np.sin(2*np.pi*297*t), 0.5*np.sin(2*np.pi*264*t)]
count = 0
freq = [ 264,297,330,352,396,440,495,528 ]

s = []
n = random.randint(0,4)

for i in range(0, len(t)):
	if(i%11025==0):	
		n = random.randint(0, 7) 
		a = random.randint(1,5) 
	s.append(a*np.sin(2*np.pi*freq[n]*t[i]))

sig_16bit = []

min_la = min( s )
max_la = max( s )
ambit = 2.0 * max(min_la, -max_la)
scale = ( 2**16 - 1 )/( ambit )
sig_16bit = [ int(scale*i) for i in s ]

objetoPyAudio = pyaudio.PyAudio()

arquivoWav = wave.open('{}.wav'.format(str(count)), 'wb')
arquivoWav.setnchannels(1)
arquivoWav.setsampwidth(2)
arquivoWav.setframerate(sr)
for i in sig_16bit:
	# Faca do 'i' uma variavel c “short signed” e escreva no arquivo
	arquivoWav.writeframes(struct.pack('h',i))
arquivoWav.close() 
count += 1

 
plt.figure(1)
plt.title('Sinal Audio gravado')
plt.plot(t, s)
plt.show()   

# min_la = min( la )
# max_la = max( la )
# ambit = 2.0 * max(min_la, -max_la)
# scale = ( 2**16 - 1 )/( ambit )
# sig_16bit = [ int(scale*i) for i in la ]
  
# objetoPyAudio = pyaudio.PyAudio()

# arquivoWav = wave.open('tone_220.wav', 'wb')
# arquivoWav.setnchannels(1)
# arquivoWav.setsampwidth(2)
# arquivoWav.setframerate(sr)
# for i in sig_16bit:
# 	# Faca do 'i' uma variavel c “short signed” e escreva no arquivo
# 	arquivoWav.writeframes(struct.pack('h',i))
# arquivoWav.close() 