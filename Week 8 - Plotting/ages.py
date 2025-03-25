# ages.py
# This program makes a list called ages that has the same number random values as salaries (range:21 to 65) . Also has a scatter plot
# author: Loic Bagnoud

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

minsalary = 20000
maxsalary = 80000
number_of_Entries = 100

np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, number_of_Entries)
ages = np.random.randint(low = 21, high = 65, size = number_of_Entries)

# plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101, 1))
ypoints = xpoints * xpoints


sns.displot(salaries, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salaries")
plt.show()

'''
plt.plot(xpoints, ypoints, color = "red", label = "x Squared")
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("Ages")
plt.legend()
plt.show()
'''