# ____________________________________________________________
# import modules

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from dropletDynamics.solveFunctions import *


# ____________________________________________________________
# plot phik(T)

# TAIR = np.linspace(283.15, 298.15, 2)
# PHIE = np.linspace(0.40, 0.70, 2)
# Temp = np.linspace (285, 315)

# PHIK = np.zeros((len(PHIE), len(TAIR)))  # initialize lifetime matrix

# for i in range(len(PHIE)):
#     for j in range(len(TAIR)):
#         PHIK[i][j] = phik(305.15, 10**-5, TAIR[j], PHIE[i])
#         print('ok')
# phi = np.array(PHIK)


# plt.imshow(phi, interpolation="gaussian", origin="upper")
# plt.colorbar()
# plt.show()

# Phik = [phik(T, 10**-5) for T in Temp]
# plt.plot(Temp, Phik, label=('Phik'))
# plt.legend()
# plt.show()


# ____________________________________________________________
# solve equations (TAIR, PHIE)

TAIR = np.linspace(283.15, 298.15, 6)
PHIE = np.linspace(0.2, 0.8, 6)
RAD = np.linspace(1 * 10**(-6), 100 * 10**(-6), 10)

LT = np.zeros((len(PHIE), len(TAIR)))  # initialize lifetime matrix

for i in range(len(PHIE)):
    for j in range(len(TAIR)):
        variables = initVariables(305, 40 * 10**-6)
        LT[i][j] = solveEuler(variables, TAIR[j], PHIE[i])[1]
lt = np.array(LT)


# ____________________________________________________________
# plot lifetime (TAIR, PHIE)

plt.imshow(lt, origin="lower", interpolation="gaussian")
plt.xlabel('Temperature(K)')
plt.xticks([0, len(TAIR)-1], [TAIR[0], TAIR[-1]])
plt.ylabel('Relative humidity')
plt.yticks([0, len(PHIE)-1], [PHIE[0], PHIE[-1]])
plt.title('Droplet lifetime (s)')
plt.colorbar()
plt.show()


# ____________________________________________________________
# plot lifetime (RAD)

# LT = [solveEuler(initVariables(305, rad), 293.15, 0.5)[1] for rad in RAD]
# plt.plot(RAD, LT)
# plt.show()


# ____________________________________________________________
# plot int (PHIE, TAIR)

# LN = np.zeros((len(PHIE), len(TAIR)))
# inta = integrate.quad(lambda x: (3 * x / (4 * pi))**(1/3), 0, calcMass(10**(-5)))[0]

# for i in range(len(PHIE)):
#     for j in range(len(TAIR)):
#         LN[i][j] = inta * Rair * TAIR[j] / (D * log((1 - psi(TAIR[j]) * PHIE[i]) / (1 - psi(305) * 1.9 * PHIE[j])))
# ln = np.array(LN) * 10**5

# plt.imshow(ln, origin="lower", interpolation="gaussian")
# plt.xlabel('Temperature (K)')
# plt.xticks([0, len(TAIR)-1], [TAIR[0], TAIR[-1]])
# plt.ylabel('Relative humidity')
# plt.yticks([0, len(PHIE)-1], [PHIE[0], PHIE[-1]])
# plt.title('Droplet lifetime (s)')
# plt.colorbar()
# plt.show()


# ____________________________________________________________
# solve equations

variables = initVariables(305.15, 10 * 10**-6)
run = solveEuler(variables, 293.15, 0.4)
solution, lifetime = run[0], run[1]
mass = solution['mass']
temp = solution['temp']
rad = solution['rad']
time = np.linspace(0, lifetime, num=len(mass))


# ____________________________________________________________
# plot solutions

plt.plot(time, mass, label='Mass')
plt.xlabel('Time(s)')
plt.ylabel('Mass (kg)')
plt.legend()
plt.show()

plt.plot(time, temp, label='Temp')
plt.xlabel('Time(s)')
plt.ylabel('Temperature (K)')
plt.legend()
plt.show()

plt.plot(time, rad, label='Radius')
plt.xlabel('Time(s)')
plt.ylabel('Radius (m)')
plt.legend()
plt.show()

# ____________________________________________________________
# debug

# plt.plot(time[:-1], run[2], label='psat')
# plt.plot(time[:-1], run[3], label='phi')
# plt.legend()
# plt.show()
