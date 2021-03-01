# ____________________________________________________________
# import modules

from math import *
from auxiliaryFunctions import *

def solveEuler(P, Pstar):

    i = 0

    while i < 100000:

        p = P[-1]
        pstar = Pstar[-1]

        P.append(p - step * (k3 * p + k2 * pstar))
        Pstar.append(pstar + step * (k1 * h0 * p - k2 * pstar))

        i+=1

    return [P, Pstar, i]