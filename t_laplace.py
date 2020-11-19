import sympy as sym
from sympy.abc import s,t,x,y,z
import numpy as np
from sympy.integrals import inverse_laplace_transform
import matplotlib.pyplot as plt
from sympy import symbols, fraction, UnevaluatedExpr
import conta as ct

s, w = symbols('s w')

def mod(num , den):
    return np.sqrt(num)/np.sqrt(den)

def fase(num , den):
    return np.arctan(num) - np.arctan(den)


def questao1(R, C):
    H = 1 / ( s*R*C + 1)
    return H

# def questao2():
#     ws = [10, 1000, 10000]
#     C = 100 * 10**-6
#     R = 10
#     for s in ws:
#         w = s
#         v = w / (w*w + s*s)
#         h = questao1(R, C) * v
#         print(h)
#         n, d = fraction(h)
#         amp = mod(n, d)
#         print(amp)



C = 100 * 10**-6
R = 10
# Transfer function
w = 100
H = 1 / ( s*R*C + 1)
n, d = fraction(H)
mod(1, 1)
print(n,  d)
fase(n,d)

print('{}*cos({}t + {})'.format(round(mod(1,1),3), w, round(np.degrees(fase(1, w)), 3 )))

tm = np.linspace(0,8,100)
ys = np.zeros(len(tm))

# plt.figure()
# plt.plot(tm, ys, label='y(t)')
# plt.legend()
# plt.xlabel('Time')
# plt.show()