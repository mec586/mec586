# ____________________________________________________________
# import modules
import numpy as np
from math import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# ____________________________________________________________
# constants

eta = 10**(-5)
p_drop = 1000
p_air = 1.3
g = 9.81 * (1 - p_air / p_drop)
r = 0.00001
m = p_drop * (4 * pi * r**3) / 3


# ____________________________________________________________
# ode resolution

x0 = 0
z0 = 1.7
vx0 = 10
vz0 = 0
X0 = [x0, vx0]
Z0 = [z0, vz0]

t = np.linspace(0, 100, 1000)

def xderiv(X,t):
    dxdt = X[1]
    dvxdt = - 6 * pi * r * eta * X[1] / m
    return [dxdt, dvxdt]

def zderiv(Z,t):
    dzdt = Z[1]
    dvzdt = - g - 6 * pi * r * eta * Z[1] / m
    return [dzdt, dvzdt]

x, vx = odeint(xderiv, X0, t)[:, 0], odeint(xderiv, X0, t)[:, 1]
z, vz = odeint(zderiv, Z0, t)[:, 0], odeint(zderiv, Z0, t)[:, 1]

def stop(L):
    i = 0
    while i < len(L) and L[i] > 0:
        i+=1
    return i-1

istop = stop(z)

x = x[:istop]
vx = vx[:istop]
z = z[:istop]
vz = vz[:istop]
t = t[:istop]

# motion
# plt.plot(t, vx)
plt.title('z(t)')
plt.plot(t, z)
# plt.plot(t, vz)
plt.show()

# comparison drag force / gravity along movement
# plt.plot(t, (6*pi*r*eta*abs(vz))/(m*g), label = 'zdrag/g')

# plt.plot(t, vz)
# plt.plot(t, x, color = 'g')

