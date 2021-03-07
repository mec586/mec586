# ____________________________________________________________
# import modules

from math import *
import scipy.optimize as sp
from dropletDynamics.initiateConstants import *


# ____________________________________________________________
# auxiliary functions

def psat(T):  # Buck's approximation
    return 10**3 * 0.61121 * exp((18.678 - (T - 273.15) / 234.5) * (T - 273.15) / (T - 273.15 + 257.14))

def psi(T):
    return (psat(T) / pe) * (Mw / Mair)

def phik(T, a, Tair, Phie):
    def f(T, a, x):
        return fev * psat(T) * (1 - x) / sqrt(2 * pi * Rw * T) - log((1 - psi(Tair) * Phie) / (1 - psi(T) * x)) * (D * pe) / (a * Rair * Tair)
    return sp.fsolve(lambda x: f(T, a, x), 0)[0]
