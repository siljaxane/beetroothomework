x = set(["Ape", "Owl", "Cat", "Owl", "Owl", "Dog"])

print(x)

y = ("Wish you Good Luck!")

print(list(y))
print(set(y))

import random

numbers = [random.randint(1, 20) for _ in range(20)] # >> this is a list compresension

numbers
[3, 8, 19, 1, 17, 14, 6, 19, 14, 7, 6, 1, 17, 10, 8, 14, 17, 10, 2, 5]

unique_numbers = set(numbers)
{1, 2, 3, 5, 6, 7, 8, 10, 14, 17, 19}

len(unique_numbers)
11