# ____________________________________________________________
# import modules
import numpy as np
import matplotlib.pyplot as plt
from solveFunctions import *


# ____________________________________________________________
# solve equations

solution, lifetime = solveEuler(variables)[0], solveEuler(variables)[1]
time = np.linspace(0, lifetime * step, num=len(solution['Rs']))


# ____________________________________________________________
# plot solutions

# plt.plot(time, solution['Rs'], label='Rs')
plt.plot(time, solution['pmean'], label='pmean')
# plt.plot(time, solution['m1'])
# plt.plot(time, solution['m3cr'])
# plt.plot(time, solution['S'])
# plt.plot(time, solution['Ts'])
# plt.plot(time, solution['BM'])
plt.legend()
plt.show()

