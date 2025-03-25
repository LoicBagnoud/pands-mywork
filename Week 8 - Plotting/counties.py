# counties.py
# This program makes a list of counties and makes a pie chart out of them
# author: Loic Bagnoud


import numpy as np
import matplotlib.pyplot as plt

possible_counties = ["Cork", "Galway", "Dublin", "Limmerick", "Mayo"]

counties = np.random.choice(
    possible_counties, p = [0.10, 0.30, 0.20, 0.20, 0.20],
    size = 100
)

unique, counts = np.unique(counties, return_counts=True)

plt.bar(unique, counts)
plt.show()