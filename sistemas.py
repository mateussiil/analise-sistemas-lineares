import numpy as np
from scipy.integrate import odeint
from scipy.optimize import fsolve

import matplotlib.pyplot as plt
import calc

def rl_didt(i, t, V, l, r):
  """
    Sistema rc que da a carga da capacitancia em relacao a t

    E = ri + q/c
    E = r*dqdt + q/c
  """
  didt = (V - r*i )/l
  return didt

def rc_dqdt(q, t, E, r, c):
  """
  Sistema rc que da a carga da capacitancia em relacao a t

  E = ri + q/c
  E = r*dqdt + q/c
  
  """

  dqdt = (E - q/c)/r
  return dqdt

def rc_dvdt(v, t, V, r, c):
  """Sistema rc"""
  dvdt = (V- (v/r))/c
  return dvdt

def rlc(r,c,l, c1, c2, t):
  """Sistema rlc"""
  return edo2ordem(l, r, 1/c, c1, c2, t)

def massaMola(m, b, k, c1, c2, t ):
  """Sistema massa mola"""
  return edo2ordem(m,b, k, c1, c2, t)

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

def ratos(x, t):
  """ Crescimento populacional de ratos x Corujas"""
  dpdt = 0.5*x - 450
  return dpdt

def quedalivre(v, t, m, g, y):
  dvdt = -(y*v)/m + g
  return dvdt

def banco(x, t, y0, i, d):
  dpdt = i*x - d
  return dpdt

def lago(q, t):
  """ concetracao é dada por Ai=agua inicial, tx= taxa de substancia por galao, Q=quantidade de galao que entra por hora """
  c = 300*0.01 
  dqdt = c - (1000000)*c*q
  return dqdt

t  = [i/10000 for i in range(0, 60000, 1)]


# y =  odeint(ratos, 901, t)
# y1 =  odeint(ratos, 850, t)

# y1 = [i[0] for i in y1]
# print(calc.valorProximo(0, y1, t))
# print(fsolve(ratos, 850, args=(t)))

y = odeint(rl_didt, )

plt.plot(t, y)
plt.plot(t, y1)
plt.show()




