import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import calc
import cmath
import math


import funcoesElementares as sgn

t = np.arange(-5, 10, 1)

def questao1():
  x1 = sgn.u(t)
  x2 = sgn.u(t, t0=2)
  x3 = sgn.u(t, t0=4)
  x = []
  y = []

  for i in range(len(x1)):
    r = x1[i] - x2[i]
    x.append(r)

  for i in range(len(x1)):
    r = x[i] + x3[i]
    y.append(r)

  plt.xticks(t, [str(i) for i in t])
  plt.plot(t, y, drawstyle="steps-post")
  plt.show()

def rc(v, t, amp, vs):
    r = 20
    c = 2000*(10**-6)
    for i in vs:
      i = i*amp
      dvdt = i/c - v/(r*c)
    return dvdt

def questao2a(): 
  v0 = 0.5
  vs = sgn.u(t)
  v = odeint(rc, v0, t, args=(1.3, vs))
  print(v)
  plt.plot(t, v)
  plt.show()

def questao2b():
  v0 = 0.5
  vs = sgn.u(t,t0=5)
  v = odeint(rc, v0, t, args=(0.1, vs))
  print(v)
  plt.plot(t, v)
  plt.show()

def rlc(r,c,l, c1, c2, t):
  """Sistema rlc"""
  return edo2ordem(2, r, 1/c, 1, 0, t)

# plt.plot(t, calc.edo2ordem(2*10**3, 200, 1/(10*10**-6), 1, 0, t))
# plt.show()
