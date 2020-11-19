import numpy as np
import matplotlib.pyplot as plt
import operations1 
from funcoesElementares import u, delta
import calc


def questao1(a):
  """a recebe o valor de escalonamento """

  x = np.arange(-5, 6, 1)
  y = np.ones(11)
  y[0]=0
  y[-1]=0
  x1 = operations1.escalonamento(x, a)
  plt.title("x({}t)".format(a))
  plt.plot(x1, y)
  # plt.xlim(-1.2, 1.2)
  # pontos = list(range(-1, 1, 5))
  plt.xticks(x1,[str(i) for i in x1])
  plt.grid()
  plt.show()

def questao2():
  """ 2 """

  x = np.arange(-5, 6, 1)
  y = np.ones(11)
  y[0]=0
  y[-1]=0
  x1 = operations1.deslocamento(x,5)
  x2 = operations1.escalonamento(x1, 10)
  plt.title("x(10t – 5)")
  plt.plot(x2, y)
  # plt.xlim(-1.2, 1.2)
  # pontos = list(range(-1, 1, 5))
  plt.xticks(x2,[str(i) for i in x2])
  plt.grid()
  plt.show()


def questao31():
  """ 3.1 """

  t  = np.linspace(0, 6, dtype=int)
  y = delta(t=t, amp=1,t0=3)
  plt.title(" δ[n-3]]")
  plt.stem(t,y)
  plt.xticks(t,[str(i) for i in t])
  plt.show()

def questao32( ):
  """ 3.2 """
  t = np.arange(-2, 5, 1)
  y1 = u(t)
  y2 = u(t,t0=2)
  y3 = []
  for i in range(len(y1)):
    y3.append(y1[i]-y2[i])
  plt.title(" x(t) = u(t) – u(t-2)")
  plt.plot(t,y3, drawstyle="steps-post")
  plt.savefig("Plot 32")

def questao33( ):
  """ 3.3 """
  x = np.arange(-2, 5, 1, dtype=int)
  y1 = u(x,t0=-1)
  y2 = u(x,amp=2)
  y3 = u(x,t0=1)
  y4 = []
  for i in range(len(y1)):
    y4.append(y1[i]-y2[i]+y3[i])
  plt.title(" x(t) = u(t+1) – 2u(t) + u(t-1)")
  plt.xlim((-2,x[-1]))
  plt.xticks(x,[str(i) for i in x])
  plt.plot(x,y4,drawstyle="steps-post")
  plt.savefig("Plot 33")

def rlc(r, c, l, c1, c2, t):
  """ Informar c1 e c2"""  
  return calc.edo2ordem(l, r, 1/c, c1, c2, t)