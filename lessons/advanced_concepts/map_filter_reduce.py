"""Map"""

def length(n):
    return len(n)

fruits = ('apple', 'banana', 'cherry')
fruits_length = map(length, fruits)
print(fruits_length)


def combo(a, b):
    return a + b

more_fruits = map(combo, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(len(fruits))


"""Filter"""

ages = [5, 12, 17, 18, 24, 32]

def kid_filter(age):
  if age < 18:
    return False
  else:
    return True

adults = filter(kid_filter, ages)

for age in adults:
    print(age)


"""Reduce"""

from functools import reduce

number_list = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(reduce(lambda a, b: a + b, number_list))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, number_list))


# importing operator for operator functions
import operator

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(reduce(operator.add, number_list))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(reduce(operator.mul, number_list))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(reduce(operator.add, ["geeks", "for", "geeks"]))
