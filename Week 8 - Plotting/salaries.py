# salaries.py
# This program runs a random number of salaries and displays its increases as well as plots it.
# author: Loic Bagnoud

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 100

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

plt.hist(salaries)
plt.show()