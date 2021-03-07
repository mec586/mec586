# ____________________________________________________________
# import modules

from dropletDynamics.initiateVariables import *


# ____________________________________________________________
# integration step

def integrateMass(T, a, Tair, Phie):
    # return log((1 - psi(Tair) * Phie) / (1 - psi(T) * phik(T, a, Tair, Phie))) * (D * pe) / (a * Rair * Tair)
    return - log((1 - psi(Tair) * Phie) / (1 - psi(T) * phik(T, a, Tair, Phie))) * 4 * pi * pw * D * a

def integrateTemp(T, a, Tair, Phie):
    return (1 / (pw * cw)) * ((3 * kair * (Tair - T)) / a**2 - 3 * integrateMass(T, a, Tair, Phie) * Lev / a)

def integradeRad(T, a, Tair, Phie):
    return integrateMass(T, a, Tair, Phie) / (4 * pi * pw * a**2)