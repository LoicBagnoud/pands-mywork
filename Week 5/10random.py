# 10random.py
# This program puts 10 random numbers into a queue(list), 
# the program should then output all the values in the queue, 
# then take the numbers from the queue one at a time, print it and the current numbers still in the queue.
# author: Loic Bagnoud

import random
queue = []
number_of_random_numbers = 10
num_range = 100

for n in range(0, number_of_random_numbers):
    queue.append(random.randint(0, num_range))

queue.sort()

print(f"The current queue is {queue}")

while len(queue) != 0:
    current_number = queue.pop(0)
    print(f"The current number is {current_number} and the queue is {queue}")

print("The queue is now empty")