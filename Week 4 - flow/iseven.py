# iseven.py
# This program  asks the user to enter in a number, and the program will tell the user if the number is even or odd.
# author: Loic Bagnoud

number = int(input("Enter an integer (or -1 to exit): "))

if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


while number != -1:
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
    number = int(input("Enter an integer (or -1 to exit): "))         