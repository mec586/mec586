# ____________________________________________________________
# import modules

from dropletDynamics.auxiliaryFunctions import *


# ____________________________________________________________
# variables

m = 4 * pi * pw * a**3 / 3  # initial mass of water (kg)
T = 305  # initial droplet temperature (K)

variables = {}
variables['mass'] = [m]
variables['temp'] = [T]
variables['rad'] = [a]