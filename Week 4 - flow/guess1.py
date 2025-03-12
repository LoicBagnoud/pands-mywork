# guess1.py
# This program prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right on
# author: Loic Bagnoud

number_to_guess = 25

guess = int(input("Try to guess the number: "))
while guess != number_to_guess:
    print("Guess again.")
    guess = int(input("Try to guess the number again: "))

print(f"Well done. The correct number was indeed {number_to_guess}")
