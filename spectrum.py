import numpy as np
from scipy.fft import fft, fftfreq
from math import *
import matplotlib.pyplot as plt
from scipy import signal
from numpy.random import randn


def spect(s, Fs=44100):
    """
    Use as follows: plt.plot(*spect(s)); plt.show()
    """
    spec = fft(s, norm="forward")
    xf = fftfreq(spec.size, d=1/Fs)

    n = round(s.shape[0]/2)
    return xf[:n], 20*np.log10(np.abs(spec[0:n]))


def pspect(s, Fs=44100):
    plt.plot(*spect(s, Fs))
    plt.grid(True)
    plt.show()


def semispect(s, Fs=44100):
    plt.semilogx(*spect(s, Fs))
    plt.grid(True, "both")
    plt.show()
