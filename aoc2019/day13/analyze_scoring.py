import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('scoring.txt')

print(data)

blocks_remaining = data[:, 0]
score = data[:, 1]

plt.plot(score, blocks_remaining)

poly = np.poly1d(np.polyfit(blocks_remaining, score, 1))

print(poly(0))

print(np.diff(score))

plt.show()


# 12562 is too low