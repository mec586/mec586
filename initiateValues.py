# ____________________________________________________________
# import modules
from math import *
from auxiliaryFunctions import *


# ____________________________________________________________
# constants

step = 0.0001
p0 = 1013.25 * 10**2  # atmospheric pressure (Pa)
L = 2.47 * 10**6  # latent heat of vaporisation
R = 8.314462  # gas constant (J / (K.mol))
M1 = 0.01801  # molecular mass of water (kg / mol)
M2 = 0.028976  # molecular mass of air (kg / mol)
Msalt = 0.05844  # molecular mass of salt (kg / mol)
t0 = 373.15  # reference air temperature
pl = 1000  # density of liquid water (kg / m**3)
ps = 2200  # density of salt (kg / m**3)
Cp = 4.18 * 10**3  # specific heat capacity (J / (kg.K))
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
Rs = 10**-3  # initial droplet radius (m)


# ____________________________________________________________
# variables

m30 = 0.01 * 4 * pi * pl * Rs**3 / 3  # initial mass of salt, as a fraction of initial droplet mass
Ts = 305.15
X1s = 0.99
Pvap = Pvap(Ts, X1s)
pv = pv(Ts, Pvap)
BM = BM(Ts, X1s, RH, Tinf)


(m, Cpl, kg, As, Rs, , m1dot, hfg, el, )
(S, gcr, Ccr, Ea, R, , )
(ps, l, ldot, )

# ____________________________________________________________
# dictionnary

variables = {}
variables["m1dot"] = integrate15(pv0, Dv0, Rs0, Bm0, step) / step # initier tout ce qu'il y a dedans
variables["pv"] = p0 * Mwat / (R * Ts0)  # initier un Ts0
variables["Dv"] = Dv0
variables["Rs"] = Rs0
variables["BM"] = BM0
variables["Y1s"] = Y1s0
variables["Y1inf"] = Y1inf0
