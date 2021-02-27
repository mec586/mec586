# ____________________________________________________________
# import modules

from math import *
from integrateStep import *


# ____________________________________________________________
# solve functions

def solveEuler(variables):
    while (condition):

        # update values with integration step
        m1 += integrate15(pv, Dv, Rs, BM, step)
        Ts += integrate17(m, Cpl, kg, As, Rs, Tinf, m1dot, hfg, el, step)
        l += integrate19(S, gcr, Ccr, Ea, R, Ts, step)
        m3cr += integrate20(ps, l, ldot, step)

        # update variables


    return