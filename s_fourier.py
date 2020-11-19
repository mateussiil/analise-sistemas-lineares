import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import scipy as sp

time = np.arange(-2, 2, 0.1)
x = np.arange(-2, 2, 0.1)

t0 = 4
f1 = lambda t: -1*t
f2 = lambda t: 1*t
w0=2*np.pi/t0
f11 = lambda t: -1*t*np.cos(m*w0*time)
f21 = lambda t: 1*t*np.cos(m*w0*time)

s = [-1*x if x>=-2 and x<0 else x for x in time]

def a0(f, ti, ts, t0, t):
    return (1/t0)*integrate.quad(f, ti, ts)[0]

def am(f, m, ti, ts, t0, t):
    return (2/t0)*integrate.quad(f, ti, ts)[0]
    
def bm(f, m, ti, ts, t0, t):
    return (2/t0)*integrate.quad(f, ti, ts)[0]


# f_a = 2*f_s
# f_a = frequência de amostragem
# f_s frequência do sinal

# f_a >= 2*f_s

y = a0(f1, -t0/2, 0, t0, time) + a0(f2, 0, t0/2, t0, time)
M = 100
w0 = 2*sp.pi/t0
err = []
for m in range(1, M):
  # am = integrate.quad(lambda t: -t*np.cos(w0*m*t), -t0/2, 0)[0] + integrate.quad(lambda t:t*np.cos(w0*m*t), 0, t0/2)[0]
  am1 = (4/((m*np.pi)*(m*np.pi)))*(np.cos(m*np.pi) - 1)
  print(am1)
  print(am(f11, m, -t0/2, 0, t0, time) + am(f21, m, 0 , t0/2, t0, time))
  # bm, err  = integrate.quad(lambda t: -2/t0*t*np.sin(sp.pi*m*t*0.5) , -t0/2, 0)[0] + integrate.quad(lambda t: 2/t0*t*np.sin(sp.pi*m*t*0.5) , 0, t0/2)[0]
  # bm, errm= integrate.quad(lambda t: -2/t0*t*np.sin(sp.pi*m*t*0.5) if t>=-2 and t< 0 else 0.5*t*np.sin(m*sp.pi*0.5), 0, t0)
  # y += am*np.cos(m*time*sp.pi) + 0 
  y += am1*np.cos((m*time*sp.pi)/2) + 0
  err.append(s[0]-y[0])
 
  name= str('Figura {}'.format(m))

mascara = time > 0

plt.figure(1)
plt.title('Erro em funcao de t, para t>0')
plt.plot(time[mascara], abs(s - y)[mascara])
# plt.savefig("Erro em funcao de t para t maior 0")

plt.figure(2)
plt.title('real x aproximado')
plt.plot(time, s, '--')
plt.plot(x, y, '--')
# plt.savefig("real x aproximado")

plt.figure(3)
plt.title('Erro em funcao de m')
plt.plot([i for i in range(1, M)], err)
# plt.savefig("Erro em funcao de m")



#Resposta da questao 2
for i in range(1, M):
  if(err[i]<0.007):
    print('Para m={}, temos um valor de {}'.format(i, err[i]))
    break