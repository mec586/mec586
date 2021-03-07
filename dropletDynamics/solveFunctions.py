# ____________________________________________________________
# import modules

from dropletDynamics.integrateStep import *


# ____________________________________________________________
# solve functions

def solveEuler(variables, Tair, Phie):

    i = 0

    while i < 10000000 and variables['mass'][-1] > 0:

        # call values
        m, T, a = variables['mass'][-1], variables['temp'][-1], variables['rad'][-1]

        # update values with integration step
        variables['mass'].append(m + step * integrateMass(T, a, Tair, Phie))
        variables['temp'].append(T + step * integrateTemp(T, a, Tair, Phie))
        variables['rad'].append(a + step * integradeRad(T, a, Tair, Phie))

        # update iteration count
        i += 1

        print('iteration')

    return [variables, i * step]