# ____________________________________________________________
# import modules

import numpy as np
from math import *
import matplotlib.pyplot as plt


# ____________________________________________________________
# constants

p0 = 1013.25 * 10**2 # atmospheric pressure (Pa)
L = 2.47 * 10**6  # latent heat of vaporisation
R = 8.314462 # gas constant (J / (K.mol))
Mwat = 0.01801 # molecular mass of water (kg)
Mair = 0.028976 # molecular mass of air (kg)
t0 = 373.15 # reference air temperature
x = 1 # chi1, mole-fraction of evaporating water at the surface
r = 10**-4 # initial droplet radius (m)
pl = 1000 # density of liquid water (kg/m**3)
# pv = 0.013, not used because we calculate pv which is not constant



# ____________________________________________________________
# build temperature, relative humidity and vapor pressure arrays

T = np.linspace(278.15, 308.15, 50) # K
RH = np.linspace(0.40, 0.80, 50) # %
PV = [p0 * Mwat / (R * t) for t in T]


# ____________________________________________________________
# build diffusivity and vapor pressure matrices

D = np.array([-2.775 * 10**-6 + 4.479 * 10**-8 * t + 1.656 * 10**-10 * t**2 for t in T]) # regression
# PSAT = np.array([p0 * exp(L * Mwat * (1/t0 - 1/t) / R) for t in T]) # T in Kelvin
PSAT = np.array([10**3 * 0.61121 * exp((18.678 - (t - 273.15) / 234.5) * (t - 273.15) / (t - 273.15 + 257.14)) for t in T]) # Buck's equation

# psat = 4.8 * 10**3 # at 32°C
# y1 = x * psat * Mwat / (x * psat * Mwat + (1 - x * psat) * Mair)


# ____________________________________________________________
# build Spalding mass transfer number (BM) matrix

BM = np.zeros((len(RH), len(T)))

for i in range(len(RH)):
    for j in range(len(T)):
        ys = x * (PSAT[j] / p0) * Mwat / (x * (PSAT[j] / p0) * Mwat + (1 - x * (PSAT[j] / p0)) * Mair) # assume Ts = Tinf quickly
        yinf = RH[i] * (PSAT[j] / p0) * Mwat / (RH[i] * (PSAT[j] / p0) * Mwat + (1 - RH[i] * (PSAT[j] / p0) * Mair))
        BM[i][j] = (ys - yinf) / (1 - ys)


# ____________________________________________________________
# build characteristic time matrix

TAU = np.zeros((len(RH), len(T)))
for i in range(len(RH)):
    for j in range(len(T)):
        TAU[i][j] = pl * r**2 / (2 * PV[j] * D[j] * log(1 + BM[i][j]))

f = np.array(TAU)


# ____________________________________________________________
# plot

plt.imshow(f, interpolation="gaussian", origin="upper")
plt.xlabel('temp')
plt.xticks([0, len(T)-1], [T[0], T[-1]])
plt.ylabel('relative humidity')
plt.yticks([0, len(RH)-1], [RH[0], RH[-1]])
plt.colorbar()
plt.show()

# ____________________________________________________________
# debug

