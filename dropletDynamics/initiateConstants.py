# ____________________________________________________________
# import modules

from math import *


# ____________________________________________________________
# parameters

# Tair = 305  # atmospheric temperature (K)
# Phie = 0.8  # relative humidity
a = 40 * 10**-6  # initial droplet radius (m), actually a variable


# ____________________________________________________________
# constants

step = 0.000001  # integration step (s)
D = 3 * 10**(-5)  # diffusion coefficient (m**2/s)
pe = 1.015 * 10**5  # atmospheric pressure (Pa)
Rw = 461.7  # gas constant of water (J / (kg * K))
Rair = 286.5  # gas constant of air (J / (kg * K))
Mw = 18 * 10**(-3)  # molar mass of water (kg/mol)
Mair = 29 * 10**(-3)  # molar mass of air (kg/mol)
fev = 0.0024  # dimensionless coefficient accounting for air in Knudsen layer
kair = 0.026  # thermal conductivity of air (W / (m * K))
pw = 10**3  # density of water (kg / m**3)
cw = 4.18 * 10**3  # heat capacity of water (J / (kg * K))
Lev = 2.26 * 10**6  # vaporization enthalpy (J / kg)