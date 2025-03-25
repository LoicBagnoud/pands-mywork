# plotfunction.py
# This program plots the function y = x2
# author: Loic Bagnoud

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 101])
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()