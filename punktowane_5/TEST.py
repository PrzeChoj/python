import math
import random


import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

for i in range(-10, 10, 1):
    plt.scatter(i/10, math.exp(i/10)-1, color="red")






fig.savefig("funkcja.png", dpi=90)
