import numpy as np
import matplotlib.pyplot as plt
import random

time = 0
pos = 0
time_array, pos_array = [], []

while time < 400:
    time_array.append(time)
    pos_array.append(pos)

    time += np.random.poisson(2)
    pos += random.choice([-1, 1])

plt.plot(time_array, pos_array)
plt.xlabel("time")
plt.ylabel("position")
plt.show()
