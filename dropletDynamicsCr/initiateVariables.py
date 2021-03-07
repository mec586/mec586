# ____________________________________________________________
# import modules
from dropletDynamicsCr.auxiliaryFunctions import *


# ____________________________________________________________
# variables

X1s = 0.6  # initial chi1 surface
m1 = X1s * (4 * pi * pl * Rs**3) / 3  # initial mass of water
m3d = (1 - X1s) * (4 * pi * pl * Rs**3) / 3  # initial mass of salt, as a fraction of initial droplet mass
m3cr = 0  # initial mass of crystallized salt
S = s(m1, m3cr, m3d)
m = m1 + m3d + m3cr  # initial total mass of droplet
As = 4 * pi * Rs*2  # initial surface of water
Ts = 305.15  # initial temperature surface
Pvap = pvap(Ts, X1s)  # initial pressure of saturated pressure
pv = rhov(Ts, X1s)  # initial density of vapor
BM = bm(Ts, X1s, RH, Tinf)
m1dot = - 4 * pi * pv * Dv * Rs * log(1 + BM)  # initial derivative of water mass
l = 0  # initial length of crystal
ldot = (S - 1)**gcr * Ccr * exp(-Ea / (R * Ts))  # initial derivative of crystal length
pmean = rhomean(Rs, m1, m3cr, m3d)


# ____________________________________________________________
# dictionnary

variables = {}
variables['Rs'] = [Rs]
variables['m1'] = [m1]
variables['m3d'] = [m3d]
variables['m3cr'] = [m3cr]
variables['S'] = [S]
variables['m'] = [m]
variables['As'] = [As]
variables['Ts'] = [Ts]
variables['X1s'] = [X1s]
variables['Pvap'] = [Pvap]
variables['pv'] = [pv]
variables['BM'] = [BM]
variables['m1dot'] = [m1dot]
variables['l'] = [l]
variables['ldot'] = [ldot]
variables['pmean'] = [pmean]
