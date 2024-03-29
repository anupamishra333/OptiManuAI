# coding=utf-8
from industrial_benchmark_python.IDS import IDS
import numpy as np
import matplotlib.pyplot as plt


n_trajectories = 10
T = 1000

data = np.zeros((n_trajectories,T))
data_cost = np.zeros((n_trajectories,T))

for k in range(n_trajectories):
    env = IDS(p=100)
    for t in range(T):
        at = 2 * np.random.rand(3) -1
        markovStates = env.step(at)
        data[k,t] = env.visibleState()[-1]

plt.plot(data.T)
plt.xlabel('T')
plt.ylabel('Reward')
plt.show()