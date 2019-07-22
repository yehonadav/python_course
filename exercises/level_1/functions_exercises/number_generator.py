import random


def numbers(range):
    while range > 0:
        yield random.randint(0, 10001)
        range -= 1
    return
