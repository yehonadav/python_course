import random
from exercises.level_2.overloaded_function import expon, results


def try_none_and_str_or_int_or_list_expon():
    expon(None)
    if random.randint(0, 2):
        param = str
    else:
        param = int
    try:
        expon(param(random.randint(0, 5)))
    except Exception as e:
        print(e, '\n\n\n')
        expon([random.randint(0, 5), random.randint(2, 4)])


def expon_int_float_and_list():
    expon(random.randint(0, 1025))
    expon(random.randint(0, 1025) * 0.001)
    expon([random.randint(1, 101) * 68 / 47 * random.randint(1, 3) for _ in range(random.randint(0, 25))])


def slow_down(stop, start):
    if stop > 20:
        before = start - n
        if before < 1:
            before = 1
        for i in range(before, stop):
            if results[i] > 1:
                results[i] = 1 / results[i]


def create_results(res_sum, stop, n, sums):
    while res_sum > stop:
        print("sum {} > {}".format(res_sum, stop))
        start = stop
        expon_int_float_and_list()

        stop = len(results)
        slow_down(stop, start)

        # should be able to reach +5000 results
        n = int(str((n+1)*0.25*(n+1)).split('.')[0])+1
        res_sum = sum(results)
        sums[str(stop)] = res_sum

    print("sum {} < {}\n\n\n".format(res_sum, stop))
    return res_sum, stop, n


def find_best_sum_and_ratio(sums):
    # find best sum
    # find best sum ratio
    class SUM:
        def __init__(self, sum, len):
            self.sum = sum
            self.len = len
            self.ratio = sum / len

    best_sum = SUM(0, 1)
    best_sum_ratio = SUM(0, 1)

    for i in sums:
        if sums[i] > best_sum.sum:
            best_sum = SUM(sums[i], int(i))

        if sums[i] / int(i) > best_sum_ratio.ratio:
            best_sum_ratio = SUM(sums[i], int(i))

    print("best sum {} with {} results and a ratio of {}".format(best_sum.sum, best_sum.len, best_sum.ratio))
    print("best ration {} with a sum of {} and {} results".format(best_sum_ratio.ratio, best_sum_ratio.sum,
                                                                  best_sum_ratio.len))


if __name__ == "__main__":
    try_none_and_str_or_int_or_list_expon()

    n, stop = 0, len(results)
    res_sum = sum(results)
    sums = {str(stop): res_sum}

    res_sum, stop, n = create_results(res_sum, stop, n, sums)
    find_best_sum_and_ratio(sums)
