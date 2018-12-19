import matplotlib.pylab as plt

x = [1, 2, 3, 4]
y = [4, 3, 5, 1]

plt.figure(figsize=[6, 6], dpi=72)

plt.subplot(1, 1, 1)

plt.scatter(x, y, color = "green", alpha=0.9, marker="x")

plt.savefig("test.png")