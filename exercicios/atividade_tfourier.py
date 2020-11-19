import numpy as np
import matplotlib.pyplot as plt
from sinais_elementares import u,delta
from scipy.fft import fft, ifft
from t_fourier import t_fourier


def plot(t, y, f, fft, amplitudes):
  plt.figure(1)
  plt.title("x(t)")
  plt.plot(t, y)

  plt.figure(2)
  plt.title("|X(w)| - espectro de amplitude")
  plt.ylabel("Amplitude")
  plt.xlabel("Frequência (Hz)")
  plt.plot(f, fft)

  plt.figure(3)
  plt.ylabel("Amplitude")
  plt.title("espectro de fase")
  plt.xlabel("Frequência (Hz)")
  plt.semilogx(f[f>0], amplitudes[f>0])

  plt.show()

def questao1():
  x = lambda t: np.exp(-10*t)*u(t) 
  N = 1000
  t0=-10
  t1=10
  time = np.linspace(t0, t1, 100)
  t = np.linspace(t0, t1, N)
  y = x(time)
  fft, f, amplitudes = t_fourier(y, len(y), t1-t0)
  y = x(t)
  
  plot(time, y, f, fft, amplitudes)


def questao2():
  t0=-10
  t1=10
  time = np.arange(t0, t1, dtype=int)
  y = delta(time)
  fft, f, amplitudes = t_fourier(y, len(y),t1-t0)

  plot(time, y, f, fft, amplitudes)

def questao3():
  N = 100
  t0=-10
  t1=10
  time = np.linspace(t0, t1, N)

  x = lambda t: np.cos(2*t) 
  y = x(time)

  fft, f, amplitudes = t_fourier(y, len(y), t1-t0)
  
  plot(time, y, f, fft, amplitudes)
