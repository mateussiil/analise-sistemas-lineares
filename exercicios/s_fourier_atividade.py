import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import scipy as sp

time = np.arange(-2, 2, 0.1)
x = np.arange(-2, 2, 0.1)


# f = lambda t: -1*t 

# def a0(f, t0, t):
#   return integrate.quad(f, -t0/2, 0)[0] + integrate.quad(f , 0, t0/2)[0]

# print(a0(f, 4, time))

t0 = 4
s = [-1*x if x>=-2 and x<0 else x for x in time]

a0 = integrate.quad(lambda t: -1*t , -t0/2, 0)[0] + integrate.quad(lambda t: -1*t , -t0/2, 0)[0]
a0 = a0/t0
y = a0
M = 100
w0 = 2*sp.pi/t0
err = []
for m in range(1, M):
  # am = integrate.quad(lambda t: -t*np.cos(w0*m*t), -t0/2, 0)[0] + integrate.quad(lambda t:t*np.cos(w0*m*t), 0, t0/2)[0]
  am = (4/((m*np.pi)*(m*np.pi)))*(np.cos(m*np.pi) - 1)
  # bm, err  = integrate.quad(lambda t: -2/t0*t*np.sin(sp.pi*m*t*0.5) , -t0/2, 0)[0] + integrate.quad(lambda t: 2/t0*t*np.sin(sp.pi*m*t*0.5) , 0, t0/2)[0]
  # bm, errm= integrate.quad(lambda t: -2/t0*t*np.sin(sp.pi*m*t*0.5) if t>=-2 and t< 0 else 0.5*t*np.sin(m*sp.pi*0.5), 0, t0)
  # y += am*np.cos(m*time*sp.pi) + 0 
  y += am*np.cos((m*time*sp.pi)/2) + 0
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

plt.show()


#Resposta da questao 2
for i in range(1, M):
  if(err[i]<0.007):
    print('Para m={}, temos um valor de {}'.format(i, err[i]))
    break