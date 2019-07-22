import random
from exercises.level_1.functions_exercises.number_generator import numbers


def create_numbers(): return [n for n in numbers(random.randint(0, 10))]


def avg(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return float(sum)/len(numbers)


def print_average(numbers):
    try:
        print(avg(numbers))
    except TypeError as e:
        print("TypeError:", e)
        return e
    except ZeroDivisionError as e:
        print("ZeroDivisionError:", e)
        return e


if __name__ == "__main__":
    while True:
        if print_average(create_numbers()):
            break
