# div.py
# This program that reads in two numbers and divides the first one by the second and give the integer result and the remainder.
# author: Loic Bagnoud

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x // y
remainder = x%y
print(f"{x} divided by {y} is {answer} and the remainder is {remainder}")