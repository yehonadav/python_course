"""
what are python lambdas ?
    A lambda function is a small anonymous function.
    A lambda function can take any number of arguments, but can only have one expression.
    The expression is executed and the result is returned

Syntax
    lambda arguments : expression

examples:
"""

compute1 = lambda x: x**x
print(compute1(5))

# add 10 to the number passed in as an argument, and print the result:
compute2 = lambda a : a + 10
print(compute2(5))

# Lambda functions can take any number of arguments
# multiply argument 'a' with argument 'b' and print the result
compute3 = lambda a, b : a * b
print(compute3(10, 10))

# sum arguments a, b, and c and print the result
compute4 = lambda a, b, c : a + b + c
print(compute4(5, 6, 2))


"""
Why are Python lambdas useful?
https://stackoverflow.com/questions/890128/why-are-python-lambdas-useful

Python supports a style of programming called functional programming
where you can pass functions to other functions to do stuff.
The power of lambda is better shown when you use them as an anonymous function inside another function.
"""

# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:
def multiply_by(n):
    return lambda a: a * n

double_trouble = multiply_by(2)
triple_trouble = multiply_by(3)

print(double_trouble(2))
print(triple_trouble(3))
# This is often used to create function wrappers, such as Python's decorators.
print(multiply_by(4)(4))

# we can use lambdas on filters
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
odds = filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(evens)
print(odds)

# VS

def evens_filter(x):
    return x % 2 == 0

def odds_filter(x):
    return x % 2 != 0

evens = filter(evens_filter, [1, 2, 3, 4, 5, 6, 7, 8, 9])
odds = filter(odds_filter, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# VS

evens = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 2 == 0]
odds = [x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9] if x % 2 != 0]

# VS

evens = [x for x in range(0,10,2)]
odds = [x for x in range(1,10,2)]

# lambdas with reduce()
from functools import reduce

combo1 = reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
combo2 = reduce(lambda a, b: a+b, [1, 2, 3, 4])
print(combo1)
print(combo2)

# Sorting by an alternate key
cool_sort = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))  # closest to 5
print(cool_sort)

