# ____________________________________________________________
# import modules
from math import *
from auxiliaryFunctions import *


# ____________________________________________________________
# constants

step = 0.0001  # integration step (s)
p0 = 1013.25 * 10**2  # atmospheric pressure (Pa)
# L = 2.47 * 10**6  # latent heat of vaporisation
R = 8.314462  # gas constant (J / (K.mol))
M1 = 0.01801  # molecular mass of water (kg / mol)
M2 = 0.028976  # molecular mass of air (kg / mol)
Msalt = 0.05844  # molecular mass of salt (kg / mol)
t0 = 373.15  # reference air temperature
pl = 1000  # density of liquid water (kg / m**3)
ps = 2200  # density of salt (kg / m**3)
Cpl = 4.18 * 10**3  # specific heat capacity (J / (kg.K))
kg = 26 * 10**-3  # conductivity of air (W / (m.K))
hfg = 2430 * 10**3  # specific latent heat of vaporization of liquid water (J / kg)
el = 105 * 10**3  # specific internal energy of liquid vaper at 25° (J / kg), depends on T
Ccr = 1.14 * 10**4  # (m/s)
Ea = 58180  # activation energy (J / mol)
gcr = 1
Y3c = 0.393
Dv = Dv(Tinf)  # diffusivity of water vapor (m**2/s)


# ____________________________________________________________
# parameters

Tinf = 300  # atmospheric temperature (K)
RH = 0.60  # relative humidity
Rs = 10**-3  # initial droplet radius (m), actually a variable


# ____________________________________________________________
# variables

m1 = 0.99 * 4 * pi * pl * Rs**3 / 3  # initial mass of water
m3d = 0.01 * 4 * pi * pl * Rs**3 / 3  # initial mass of salt, as a fraction of initial droplet mass
m3cr = 0  # initial mass of crystallized salt
S = S(m1, m3cr, m3d)
m = m1 + m3d + m3cr  # initial total mass of droplet
As = 4 * pi * Rs*2  # initial surface of water
Ts = 305.15  # initial temperature surface
X1s = 0.99  # initial chi1 surface
Pvap = Pvap(Ts, X1s)  # initial pressure of saturated pressure
pv = pv(Ts, Pvap)  # initial vapor pressure
BM = BM(Ts, X1s, RH, Tinf)
m1dot = integrate15(pv, Dv, Rs, BM, step) / step  # initial derivative of water mass
l = 0  # initial length of crystal
ldot = integrate19(S, gcr, Ccr, Ea, Ts, step) / step  # initial derivative of crystal length
pmean = pmean(Rs, m1, m3cr, m3d)


# ____________________________________________________________
# dictionnary

variables = {}
variables[Rs] = Rs
variables[m1] = m1
variables[m3d] = m3d
variables[m3cr] = m3cr
variables[S] = S
variables[m] = m
variables[As] = As
variables[Ts] = Ts
variables[X1s] = X1s
variables[Pvap] = Pvap
variables[pv] = pv
variables[BM] = BM
variables[m1dot] = m1dot
variables[l] = l
variables[ldot] = ldot
variables[pmean] = pmean
