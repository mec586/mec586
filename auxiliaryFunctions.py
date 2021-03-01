# ____________________________________________________________
# import modules

from math import *
from initiateConstants import *

# ____________________________________________________________
# auxiliary functions

def Psat(Ts):
    return 10**3 * 0.61121 * exp((18.678 - (Ts - 273.15) / 234.5) * (Ts - 273.15) / (Ts - 273.15 + 257.14))

def pvap(Ts, X1s):
    return X1s * Psat(Ts)

# def dv(Tinf):  # not used because initiated in initiateConstants
#     return -2.775 * 10 ** -6 + 4.479 * 10 ** -8 * Tinf + 1.656 * 10 ** -10 * Tinf ** 2

def rhov(Ts, X1s):
    return pvap(Ts, X1s) * M1 / (R * Ts)  # try with p0 if doesn't work

def y1s(Ts, X1s):
    return pvap(Ts, X1s) * M1 / (pvap(Ts, X1s) * M1 + (p0 - pvap(Ts, X1s)) * M2)  # actually not p0 but p0 + 2gamma/R

def x1s(m1, m3cr, m3d):
    return (m1 * M3) / (m1 * M3 + (m3cr + m3d) * M1)

def y1inf(RH, Tinf):
    return RH * Psat(Tinf) * M1 / (RH * Psat(Tinf) * M1 + (p0 - RH *  Psat(Tinf)) * M2)  # actually not p0 but p0 + 2gamma/R

def bm(Ts, X1s, RH, Tinf):
    return (y1s(Ts, X1s) - y1inf(RH, Tinf)) / (1 - y1s(Ts, X1s))

def s(m1, m3cr, m3d):
    return m3d / (Y3c * (m1 + m3cr + m3d))

def rhomean(Rs, m1, m3cr, m3d):
    m = m1 + m3cr + m3d
    return (3 / (4 * pi * Rs**3)) * m

def rs(m1, m3cr, m3d, pmean):
    return (3 * (m1 + m3cr + m3d) / (4 * pi * pmean))**(1/3)

def area(Rs):
    return 4 * pi * Rs**2
