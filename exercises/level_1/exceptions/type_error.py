import random
from exercises.level_1.exceptions.zero_division import avg, create_numbers, print_average


def randomly_stringify_list_items(numbers):
    for i in range(len(numbers)):
        if random.randint(0, 8) == 0:
            numbers[i] = str(numbers[i])


if __name__ == "__main__":
    while True:
        numbers = create_numbers()
        randomly_stringify_list_items(numbers)
        if print_average(numbers):
            break
