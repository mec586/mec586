# ____________________________________________________________
# import modules
from dropletDynamics.initiateVariables import *


# ____________________________________________________________
# integration step

def integrate15(pv, Dv, Rs, BM, step):
    return step * (- 4 * pi * pv * Dv * Rs * log(1 + BM))

def integrate17(m, As, Rs, Tinf, m1dot, step):
    return step * (1 / (m * Cpl)) * (- kg * As * (Ts - Tinf) / Rs + m1dot * (hfg - el))

def integrate18():
    return

def integrate19(S, Ts, step):
    return step * (S - 1)**(gcr) * Ccr * exp(-Ea / (R * Ts))

def integrate20(ps, l, ldot, step):
    return step * 6 * ps * (2 * l)**2 * ldot


