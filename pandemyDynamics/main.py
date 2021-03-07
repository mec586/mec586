# ____________________________________________________________
# import modules

import numpy as np
import matplotlib.pyplot as plt
from pandemyDynamics.solveFunctions import *

# ____________________________________________________________
# solve equations

solution = solveEuler([0.1], [0], [0.9], [0], [0])
P, Pstar, H, R ,X, duration = solution[0], solution[1], solution[2], solution[3], solution[4], solution[5]


# ____________________________________________________________
# plot solutions

time = np.linspace(0, duration * step, num=len(P))
plt.plot(time, P, label='P', color='g')
plt.plot(time, Pstar, label='Pstar', color='r')
plt.plot(time, H, label='H', color='b')
plt.plot(time, R, label='R', color='c')
plt.plot(time, X, label='X', color='m')
plt.legend()
plt.show()




