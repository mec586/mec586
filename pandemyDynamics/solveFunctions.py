# ____________________________________________________________
# import modules

from math import *
from pandemyDynamics.auxiliaryFunctions import *


# ____________________________________________________________
# import modules

def solveEuler(P, Pstar, H, R ,X):

    i = 0

    while i < 40000:

        p = P[-1]
        pstar = Pstar[-1]
        h = H[-1]
        r = R[-1]
        x = X[-1]

        P.append(p + step * (k2 * pstar - k3 * p))
        Pstar.append(pstar + step * (k1 * h * p - k2 * pstar))
        H.append(h - step * k1 * h * p)
        R.append(r + step * 0.97 * k3 * p)
        X.append(x + step * 0.03 * k3 * p)

        i+=1

    return [P, Pstar, H, R, X, i]