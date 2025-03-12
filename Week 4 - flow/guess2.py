# guess2.py
# This program tells the user if there guess is too high or too low, each time they guess. 
# author: Loic Bagnoud

import random

number_to_guess = random.randrange(0,101)

guess = int(input("Try to guess the number: "))
while guess != number_to_guess:
    if guess < number_to_guess:
        print("Too low. Guess again")
    else:
        print("Too high. Guess again")

    guess = int(input("Try to guess the number again: "))

print(f"Well done. The correct number was indeed {number_to_guess}")
