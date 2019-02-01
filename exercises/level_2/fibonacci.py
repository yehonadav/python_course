def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_iterator(start, end):
    for cur in fibonacci_generator():
        if cur > end:
            return
        if cur >= start:
            yield cur


def fibonacci_sequence(x):
    if x < 2:
        return [i for i in range(x+1)]
    ans = fibonacci_sequence(x-1)
    return ans + [ans[-1] + ans[-2]]


if __name__ == "__main__":
    print(fibonacci_sequence(10))
    for i in fibonacci_iterator(5, 89):
        print(i)
