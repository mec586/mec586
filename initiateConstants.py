# ____________________________________________________________
# import modules
from math import *


# ____________________________________________________________
# parameters

Tinf = 290  # atmospheric temperature (K)
RH = 0.60  # relative humidity
Rs = 10**-5  # initial droplet radius (m), actually a variable


# ____________________________________________________________
# constants

step = 0.0000001  # integration step (s)
p0 = 1013.25 * 10**2  # atmospheric pressure (Pa)
# L = 2.47 * 10**6  # latent heat of vaporisation
R = 8.314462  # gas constant (J / (K.mol))
M1 = 0.01801  # molecular mass of water (kg / mol)
M2 = 0.028976  # molecular mass of air (kg / mol)
M3 = 0.05844  # molecular mass of salt (kg / mol)
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
Dv = -2.775 * 10 ** -6 + 4.479 * 10 ** -8 * Tinf + 1.656 * 10 ** -10 * Tinf ** 2  # diffusivity of water vapor (m**2/s)
