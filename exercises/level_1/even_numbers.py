from exercises.level_1.number_generator import numbers


class MaxLengthException(Exception):
    pass


if __name__ == "__main__":
    # even = [n for n in numbers(40) if n%2 == 0]
    even = []
    for n in numbers(40):
        if n % 2 == 0:
            if len(even) > 10:
                raise MaxLengthException('the even list has exceeded its limit of 10 items')
            even.append(n)
    print(even)
