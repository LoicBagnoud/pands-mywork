# guess2.py
# This program that keeps reading numbers until the user enters a 0. It then prints all those numbers and gives their average.
# author: Loic Bagnoud



numbers = []

number = int(input("Please enter a number (Press 0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("Please enter a number (Press 0 to quit): "))

# Print each number in the list
for value in numbers:
    print(value)

# Calculate the average once after printing all numbers
average = float(sum(numbers) / len(numbers))
print(f"The average is {average}")