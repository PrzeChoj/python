import math
import random


import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_xlim([-1.5, 1])
ax.set_ylim([-1, 2.5])

xy = [ [0, -1], [-1, 0], [0, 1], [-0.5, 2], [-1.1, 0] ]

ax.add_patch(patches.Polygon(xy, facecolor="0.75"))


"""
for i in range(-10, 10, 1):
    plt.scatter(i/10, math.exp(i/10)-1, color="red")
"""

print(xy)



fig.savefig("wykres.png", dpi=90)
