
import random

numbers = []
for i in range(50):
    numbers.append(random.randint(1, 20))

print(numbers)

occur = dict()
for num in numbers:
    if num in occur.keys():
        occur[num] += 1
    else:
        occur[num] = 1

print(occur)
#  1, 1, 3, 2, 2, 4 -- numbers
# {1: 1, 1000000000: 3} -- occur
