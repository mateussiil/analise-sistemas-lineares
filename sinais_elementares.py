import numpy as np

def u(t, amp=1, t0=0): 
    """Funcao degrau"""
    return [amp if i - t0 >= 0 else 0 for i in t]

def delta(t, amp=1, t0=0):
        
    """ Funcao impulso

    Parâmetros:
        t List: tempo.
        amp Number: Amplitude do sinal.
        t0 Number: Deslocamento do sinal.

    Retorno:
        list: lista contendo a resolucao da funcao impulso para, determinado t, amp e t0
    """
    return [ amp if i - t0 == 0 else 0 for i in t]
 
def r(t, amp=1, t0=0): 
    """Funcao rampa"""
    return [ i if i - t0 >= 0 else 0 for i in t]

def rec(t, amp=1, t0=0): 
    """Funcao reta"""
    """REFATORAR"""
    return [u(t, t0=-0.5) - u(t, t0=0.5) for i in t]