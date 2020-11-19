import math
import cmath
import sys

def edo2ordem(a,b,c,c1,c2,t,d=0):
  """ Resolve edo de 2 ordem homogenea"""
  delta = b*b - 4*a*c
  r1  = (-b + cmath.sqrt(delta))/(2*a)
  r2  = (-b - cmath.sqrt(delta))/(2*a)
  y = []
  print('Delta', delta)
  print('r1', r1)
  print('r2', r2)
  if delta>0:
    # Primeiro caso;
    for i in t:
      y.append(c1*math.exp(r1.real * i) + c2*math.exp(r2.real * i))
  elif delta == 0:
    # Segundo caso;
    for i in t:
      y.append(c1*math.exp(r1.real * i) + c2*i*math.exp(r2.real * i))
  else:
    #3 caso
    for i in t:
      y.append( math.exp(r1.real * i) * ( c1*math.cos(r1.imag * i) + c2*math.sin(r1.imag * i)))
  return y

def valorProximo(v, l, t):
  
    """ Busca na lista o valor mais próximo de um valor.

    Parâmetros:
        v number: Numero a ser procurado.
        l list: Lista de números a ser verificada.
        t list: Lista de tempos.

    Retorno:
        numérico: Valor mais próximo e o tempo.
    """
    menor: int = sys.maxsize   
     # -1 se nao achou menor valor
    indice= -1
    diffs = {value: [abs(value - v), time] for value, time  in zip(l, t)}
    
    return diffs.get(min(diffs, key=diffs.get))