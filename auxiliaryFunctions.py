# ____________________________________________________________
# import modules

from math import *
from initiateValues import *

# ____________________________________________________________
# auxiliary functions

def Psat(Ts):
    return 10 ** 3 * 0.61121 * exp((18.678 - (Ts - 273.15) / 234.5) * (Ts - 273.15) / (Ts - 273.15 + 257.14))

def Pvap(Ts, X1s):
    return X1s * Psat(Ts)

def Dv(Tinf):
    return -2.775 * 10 ** -6 + 4.479 * 10 ** -8 * Tinf + 1.656 * 10 ** -10 * Tinf ** 2

def pv(Ts, Pvap):
    return Pvap * M1 / (R * Ts)  # tester avec p0 si probleme

def Y1s(Ts, X1s):
    return Pvap(Ts, X1s) * M1 / (Pvap(Ts, X1s) * M1 + (1 - Pvap(Ts, X1s)) * M2)

def Y1inf(RH, Tinf):
    return RH * Psat(Tinf) * M1 / (RH * Psat(Tinf) * M1 + (1 - RH *  Psat(Tinf)) * M2)

def BM(Ts, X1s, RH, Tinf):
    return (Y1s(Ts, X1s) - Y1inf(RH, Tinf)) / (1 - Y1s(Ts, X1s))

def S(m1, m3cr, m3d):
    return m3d / (m1 + m3cr + m3d)

def pmean(Rs, m1, m3cr, m3d):
    m = m1 + m3cr + m3d
    return (3 / (4 * pi * Rs**3)) * m
