import numpy as np
import matplotlib.pyplot as plt

def shift(x, t0):
  """ Funcao de deslocamento """
  return [i+t0 for i in x]

def scaling(x, a):
  """ x(x - a)"""
  return [i/a for i in x]

def reflection(x):
  return x[::-1]



