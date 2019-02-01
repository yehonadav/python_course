def get_fib_sum(sum):
    f = []
    n_minus_1 = 0
    n = 1
    while n < sum:
        f.append(n_minus_1)
        n, n_minus_1 = n_minus_1 + n, n
    return f


print(sum(get_fib_sum(21)))
