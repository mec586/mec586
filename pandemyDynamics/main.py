# ____________________________________________________________
# import modules

import numpy as np
import matplotlib.pyplot as plt
from solveFunctions import *

# ____________________________________________________________
# solve equations

P, Pstar, duration = solveEuler([0.001], [0])[0], solveEuler([0.001], [0])[1],solveEuler([0.001], [0])[2]


# ____________________________________________________________
# plot solutions

time = np.linspace(0, duration * step, num=len(P))
plt.plot(time, P, label='P')
plt.show()
plt.plot(time, Pstar, label='Pstar')
plt.show()



