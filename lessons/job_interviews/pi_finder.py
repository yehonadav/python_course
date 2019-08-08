from random import uniform
from math import sqrt


def pi_finder(n, r):
    inside = 0
    for i in range(n):
        x = uniform(-sqrt(r), sqrt(r))
        y = uniform(-sqrt(r), sqrt(r))
        if x**2 + y**2<= r:
            inside += 1
    return inside/n*4

print(pi_finder(10, 10))
