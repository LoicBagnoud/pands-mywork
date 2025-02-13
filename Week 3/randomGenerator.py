# randomGenerator.py
# This program prints out a random number between 1 and 10.
# author: Loic Bagnoud

import random

x = int(input("Enter first number in the range to be randomised: "))
y = int(input("Enter the second number in the range to be randomised: "))


number = random.randint(x,y)
print(f"Here is a random number {number}")
