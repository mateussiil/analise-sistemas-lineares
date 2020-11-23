import numpy as np

def u(t, amp=1, t0=0): 
    """ Funcao Degrau

    Parâmetros:
        t List: tempo.
        amp Number: Amplitude do sinal.
        t0 Number: Deslocamento do sinal.

    Retorno:
        list: lista contendo a resolucao da funcao degrau para um determinado t, amp e t0
    """
    return [amp if i - t0 >= 0 else 0 for i in t]

def delta(t, amp=1, t0=0):
        
    """ Funcao impulso

    Parâmetros:
        t List: tempo.
        amp Number: Amplitude do sinal.
        t0 Number: Deslocamento do sinal.

    Retorno:
        list: lista contendo a resolucao da funcao impulso para um determinado t, amp e t0
    """
    return [ amp if i - t0 == 0 else 0 for i in t]
 
def r(t, amp=1, t0=0): 
    """ Funcao Rampa

    Parâmetros:
        t List: tempo.
        amp Number: Amplitude do sinal.
        t0 Number: Deslocamento do sinal.

    Retorno:
        list: lista contendo a resolucao da Rampa para um determinado t, amp e t0
    """
    return [ i if i - t0 >= 0 else 0 for i in t]

def rect(t, amp=1, t0=0): 
    """ Funcao rect

    Parâmetros:
        t List: tempo.
        amp Number: Amplitude do sinal.
        t0 Number: Deslocamento do sinal.

    Retorno:
        list: lista contendo a resolucao da rect para um determinado t, amp e t0
    """
    return [0 if abs(i - t0) > 0.5 else 0.5 if abs(i  - t0)==0.5 else 1 for i in t]


def triangle(t, amp=1, t0=0): 
    """ Funcao rect

    Parâmetros:
        t List: tempo.
        amp Number: Amplitude do sinal.
        t0 Number: Deslocamento do sinal.

    Retorno:
        list: lista contendo a resolucao da triangle para um determinado t, amp e t0
    """

    return [0 if abs(i - t0) >= 0.5 else 1 - 2*abs(i - t0) if abs(i  - t0) < 0.5 else 0 for i in t]
