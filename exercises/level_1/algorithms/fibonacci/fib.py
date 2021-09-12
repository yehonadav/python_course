calc = [0, 1, 1]


def fib(n: int) -> int:
    i = len(calc) - 1
    while i < n:
        calc.append(calc[i - 1] + calc[i])
        i += 1
    return calc[n]
