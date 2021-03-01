# ____________________________________________________________
# import modules

from math import *
from integrateStep import *


# ____________________________________________________________
# solve functions

def solveEuler(variables):

    Rs0 = variables['Rs'][-1]
    i = 0  # to calculate droplet lifetime

    while variables['Rs'][-1] > 0.1 * Rs0 and i < 1000000:
    # while i < 1000000:

        # call dictionnary values
        m1, Ts, l, m3cr = variables['m1'][-1], variables['Ts'][-1], variables['l'][-1], variables['m3cr'][-1]
        pmean, Rs, S = variables['pmean'][-1], variables['Rs'][-1], variables['S'][-1]
        m, As, X1s = variables['m'][-1], variables['As'][-1], variables['X1s'][-1]
        Pvap, pv, BM = variables['Pvap'][-1], variables['pv'][-1], variables['BM'][-1]
        m1dot, ldot, m3d = variables['m1dot'][-1], variables['ldot'][-1], variables['m3d'][-1]

        # update values with integration step
        variables['m1'].append(variables['m1'][-1] + integrate15(pv, Dv, Rs, BM, step))
        variables['Ts'].append(variables['Ts'][-1] + integrate17(m, As, Rs, Tinf, m1dot, step))
        variables['l'].append(variables['l'][-1] + integrate19(S, Ts, step))
        variables['m3cr'].append(variables['m3cr'][-1] + integrate20(ps, l, ldot, step))
        variables['m3d'].append(variables['m3d'][-1] - integrate20(ps, l, ldot, step))

        # update variables
        variables['m'].append(variables['m1'][-1] + variables['m3cr'][-1] + variables['m3d'][-1])
        variables['X1s'].append(x1s(m1, m3cr, m3d))
        variables['S'].append(s(m1, m3cr, m3d))
        variables['Pvap'].append(pvap(Ts, X1s))
        variables['pv'].append(rhov(Ts, X1s))
        variables['BM'].append(bm(Ts, X1s, RH, Tinf))
        variables['ldot'].append(integrate19(S, Ts, step) / step)

        variables['Rs'].append(rs(m1, m3cr, m3d, pmean))  # assume pmean is nearly constant and can be actualized after
        variables['pmean'].append(rhomean(Rs, m1, m3cr, m3d))
        variables['As'].append(area(Rs))
        variables['m1dot'].append(integrate15(pv, Dv, Rs, BM, step) / step)

        # update iteration counter
        i += 1

    return [variables, i]
