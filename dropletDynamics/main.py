# ____________________________________________________________
# import modules

import numpy as np
import matplotlib.pyplot as plt
from dropletDynamics.solveFunctions import *


# ____________________________________________________________
# plot phik(T)

# Temp = np.linspace (285, 315)
# Phik = [phik(T, 10**-5) for T in Temp]
# plt.plot(Temp, Phik, label=('Phik'))
# plt.legend()
# plt.show()


# ____________________________________________________________
# solve equations (TAIR, PHIE)

TAIR = np.linspace(288.15, 308.15, 3)
PHIE = np.linspace(40, 80, 3)

LT = np.zeros((len(PHIE), len(TAIR)))  # initialize lifetime matrix

for i in range(len(PHIE)):
    for j in range(len(TAIR)):
        LT[i][j] = solveEuler(variables, TAIR[j], PHIE[i])[1]
lt = np.array(LT)


# ____________________________________________________________
# plot lifetime (TAIR, PHIE)

plt.imshow(tau, interpolation="gaussian", origin="upper")
# plt.xlabel('temp')
# plt.xticks([0, len(TAIR)-1], [TAIR[0], TAIR[-1]])
# plt.ylabel('relative humidity')
# plt.yticks([0, len(PHIE)-1], [PHIE[0], PHIE[-1]])
plt.colorbar()
plt.show()


# ____________________________________________________________
# solve equations

# run = solveEuler(variables, Tair, Phie)
# solution, lifetime = run[0], run[1]
# mass = solution['mass']
# temp = solution['temp']
# rad = solution['rad']
# time = np.linspace(0, lifetime * step, num=len(mass))


# ____________________________________________________________
# plot solutions

# plt.plot(time, mass, label='mass')
# plt.legend()
# plt.show()

# plt.plot(time, temp, label='temp')
# plt.legend()
# plt.show()

# plt.plot(time, rad, label='rad')
# plt.legend()
# plt.show()


# ____________________________________________________________
# debug

# plt.plot(time[:-1], run[2], label='psat')
# plt.plot(time[:-1], run[3], label='phi')
# plt.legend()
# plt.show()
