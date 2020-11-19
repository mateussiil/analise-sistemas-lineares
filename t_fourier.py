import numpy as np

def t_fourier(y, N, T=1):
      
    """ Resolve a transformada de fourier.

    Parâmetros:
        y List: função ja resolvida.
        N Number: Numero de amostras.

    Retorno, nesta ordem:
        List: transformada de fourier
        List: frequencias
        List: amplitudes
    """
    fft = np.fft.fft(y) # Calcula a transformada de fourier 
    amplitudes = np.abs(fft) # Calcula a amplitude de fourier , ajustado os valores de amostras
    f = np.fft.fftfreq(np.size(fft), 1/N)
    return fft, f, amplitudes

