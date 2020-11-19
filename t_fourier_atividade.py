import numpy as np
from scipy.fft import fft, ifft

def t_fourier(y, N):
  fft = np.fft.fft(y) # Calcula a transformada de fourier 
  amplitudes = 2.0*np.abs(fft/N) # Calcula a amplitude de fourier , ajustado os valores de amostras
  f = np.fft.fftfreq(N) 
  return fft, f, amplitudes

