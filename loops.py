def get_primes(n):
    primes = []
    for i in range(2, n):
        for x in range(2, i):
            if i%x == 0:
                break
        else:
            primes.append(i)
    return primes


def get_factorial(n):
    f = 1
    if n > 1:
        for i in range(1, n):
            f *= i
    else:
        return 0
    return f


def get_fibbo(n):
    f = []
    a, b = 0, 1
    while b < n:
        f.append(a)
        a, b = b, a + b
    return f


print(get_primes(30))
print(get_factorial(8))
print(get_fibbo(500))