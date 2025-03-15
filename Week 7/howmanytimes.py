# howmanytimes.py
# This program counts how many times it has been run
# author: Loic Bagnoud

import os

FILENAME = "count.txt"

def read_number():
    with open (FILENAME) as f:
        number = int(f.read())
        return number

def write_number (number):
    with open (FILENAME, "wt") as f:
        f.write(str(number))

if not os.path.isfile(FILENAME):
    print("The file does not exist")
    write_number(0)

num = read_number()
num += 1
print(f"We have run this file {num} times.")
write_number(num)