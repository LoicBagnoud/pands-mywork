# myfunctions.py
# This program is a function called Fibonacci that takes a number and returns a list containing a Fibonacci sequence of that many numbers
# author: Loic Bagnoud


import logging
logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number < 0:
        raise ValueError("number must be greater than 0")
    if number == 0:
        return []
    
    a, b = 0, 1
    fibonacci_sequence = [0]
    for i in range(1, number):
        fibonacci_sequence.append(b)
        a, b = b, a + b
    logging.debug("%d: %s", number, fibonacci_sequence)
    return fibonacci_sequence

'''
return_7 = [0, 1, 1, 2, 3, 5, 8]
return_11 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

assert fibonacci(7) == return_7, "incorrect number for 7"
assert fibonacci(11) == return_11, "incorrect number for 11"
assert fibonacci(0) == [], "incorrect number for 0"
assert fibonacci(1) == [0], "incorrect number for 1"
'''

try:
    fibonacci(-1)
except ValueError:
    pass
else:
    assert False, "fibonacci missing value error"
'''
if __name__ == "__main__":
    print("All good")'
'''