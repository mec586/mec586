# ____________________________________________________________
# import modules

import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ____________________________________________________________
# constants
p0 = 1013.25 * 10**2  # atmospheric pressure (Pa)
L = 2.47 * 10**6  # latent heat of vaporisation
R = 8.314462  # gas constant (J / (K.mol))
Mwat = 0.01801  # molecular mass of water (kg / mol)
Mair = 0.028976  # molecular mass of air (kg / mol)
Msalt = 0.05844  # molecular mass of salt (kg / mol)
t0 = 373.15  # reference air temperature
# x = 1  # chi1, mole-fraction of evaporating water at the surface
r0 = 10**-3  # initial droplet radius (m)
pl = 1000  # density of liquid water (kg/m**3)
msalt = 0.01 * 4 * pi * pl * r0**3 / 3  # initial mass of salt
Cp = 4.18 * 10**3  # specific heat capacity (J / (kg.K))
kg = 26 * 10**-3  # conductivity of air (W / (m.K))
hfg = 2430 * 10**3  # specific latent heat of vaporization of liquid water (J / kg)
e1 = 105 * 10**3  # specific internal energy of liquid vaper at 25° (J / kg), depends on T
# pv = 0.013, not used because we calculate pv which is not constant


# ____________________________________________________________
# calculate evaporation time

T = np.linspace(278.15, 308.15, 10)
RH = np.linspace(40, 80, 10)

# ____________________________________________________________
# calculate evaporation time

def eulerStep(r, temp, x, rh, tempinf, psatinf, yinf, d, h):

    # intermediate parameters
    psat = 10 ** 3 * 0.61121 * exp((18.678 - (temp - 273.15) / 234.5) * (temp - 273.15) / (temp - 273.15 + 257.14))  # vapor pressure
    pv = p0 * Mwat / (R * temp)  # density
    ys = x * (psat / p0) * Mwat / (x * (psat / p0) * Mwat + (1 - x * (psat / p0)) * Mair)
    mwat = 4 * pi * pl * r**3  # mass of water
    a = 4 * pi * r**2  # area of droplet
    m = mwat + msalt  # total mass of the droplet
    rdot = (pv / pl) * d * log((1 - ys) / (1 - yinf)) / r  # derivative of radius
    mdot = - 4 * pi * d * r * log((1 - ys) / (1 - yinf))  # derivative of mass

    # actualization
    r, temp, x = r - h * rdot, temp - h * ((kg * a * (temp - tempinf)) / (Cp * r * m)) + h * (mdot) * (hfg - e1) / (Cp * m), \
                 x - (h * (pv / pl) * d * log((1 - ys) / (1 - yinf)) / r) * msalt / ((Mwat * Msalt) * (mwat / Mwat + msalt / Msalt)**2)
    return r, temp, x


def solveODE(rh, tempinf, h=0.001):

    # parameters constant along the drop's life
    d = -2.775 * 10 ** -6 + 4.479 * 10 ** -8 * tempinf + 1.656 * 10 ** -10 * tempinf ** 2  # diffusivity
    psatinf = 10 ** 3 * 0.61121 * exp((18.678 - (tempinf - 273.15) / 234.5) * (tempinf - 273.15) / (tempinf - 273.15 + 257.14))  # vapor pressure in the room
    yinf = rh * (psatinf / p0) * Mwat / (rh * (psatinf / p0) * Mwat + (1 - rh * (psatinf / p0) * Mair))  # constant
    r = r0  # initial radius

    # initiation of variables
    temp = 305.15  # initial droplet temperature
    x = 0.99  # initial mol ratio

    #resolution
    i = 0
    while r > r0 / 100:
        r, temp, x = eulerStep(r, temp, x, rh, tempinf, psatinf, yinf, d, h)
        i += 1
    return i * h


# ____________________________________________________________
# calculate evaporation time

# def evapTime(t, rh):
#    d = -2.775 * 10**-6 + 4.479 * 10**-8 * t + 1.656 * 10**-10 * t**2  # diffusivity
#    psat = 10**3 * 0.61121 * exp((18.678 - (t - 273.15) / 234.5) * (t - 273.15) / (t - 273.15 + 257.14)) #water vapor
#    pv = p0 * Mwat / (R * t)  # density
#    ys = x * (psat / p0) * Mwat / (x * (psat / p0) * Mwat + (1 - x * (psat / p0)) * Mair)  # assume Ts = Tinf quickly
#    yinf = rh * (psat / p0) * Mwat / (rh * (psat / p0) * Mwat + (1 - rh * (psat / p0) * Mair))
#    bm = (ys - yinf) / (1 - ys)  # Spalding mass diffusion number
#    print(bm)
#    # print('1', ys-yinf)
#    # print('2', 1-ys)
#    # print('3', ys)
#    return 0.5 * (pl / pv) * r0**2 / (d * log(1 + bm))


# ____________________________________________________________
# build matric with results

# TAU = np.zeros((len(RH), len(T)))
# for i in range(len(RH)):
#     for j in range(len(T)):
#         TAU[i][j] = evapTime(RH[i], T[j])
# tau = np.array(TAU)

# ____________________________________________________________
# build matric with results

TAU = np.zeros((len(RH), len(T)))
for i in range(len(RH)):
    for j in range(len(T)):
        TAU[i][j] = solveODE(RH[i], T[j], h = 0.01)
tau = np.array(TAU)

# ____________________________________________________________
# plot

plt.imshow(tau, interpolation="gaussian", origin="upper")
plt.xlabel('temp')
plt.xticks([0, len(T)-1], [T[0], T[-1]])
plt.ylabel('relative humidity')
plt.yticks([0, len(RH)-1], [RH[0], RH[-1]])
plt.colorbar()
plt.show()

# tempTime = [evapTime(t, RH[0]) for t in T]
# rhTime = [evapTime(T[0], rh) for rh in RH]
# plt.plot(T, tempTime, color='r')
# plt.plot(RH, rhTime, color='b')
# plt.show()

# ____________________________________________________________
# debug

