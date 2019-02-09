from functools import singledispatch
import random


results = [random.randint(5, 30)]


@singledispatch
def expon(a):
    if len(results) > 0:
        del results[0]
    raise TypeError(str(type(a)))


@expon.register(int)
def _int(a):
    for i in range(len(results)):
        results[i] = results[i] + a*2/len(results)
    return a*2


@expon.register(list)
def _list(a):
    n = len(a)
    for i in a:
        n *= i
        results.append(i+len(results))
    return n

def _none(a): pass


expon.register(type(None), _none)


@expon.register(float)
def _float(a):
    results.append((sum(results)+a)/2)
    try:
        return results[int(a/sum(results))]
    except:
        return results


if __name__ == "__main__":
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

    n = 0
    stop = len(results)
    res_sum = sum(results)
    sums = {str(stop): res_sum}
    while res_sum > stop:
        print("sum {} > {}".format(res_sum, stop))
        start = stop
        expon(random.randint(0, 1025))
        expon(random.randint(0, 1025)*0.001)
        expon([random.randint(1, 101)*68/47*random.randint(1, 3) for _ in range(random.randint(0, 25))])
        stop = len(results)
        if stop > 20:
            before = start-n
            if before < 1:
                before = 1
            for i in range(before, stop):
                if results[i] > 1:
                    results[i] = 1/results[i]
        # should be able to reach +5000 results
        n = int(str((n+1)*0.25*(n+1)).split('.')[0])+1
        res_sum = sum(results)
        sums[str(stop)] = res_sum

    print("sum {} < {}\n\n\n".format(res_sum, stop))

    # find best sum
    # find best sum ratio
    class SUM:
        def __init__(self, sum, len):
            self.sum = sum
            self.len = len
            self.ratio = sum/len

    best_sum = SUM(0, 1)
    best_sum_ratio = SUM(0, 1)

    for i in sums:
        if sums[i] > best_sum.sum:
            best_sum = SUM(sums[i], int(i))

        if sums[i]/int(i) > best_sum_ratio.ratio:
            best_sum_ratio = SUM(sums[i], int(i))

    print("best sum {} with {} results and a ratio of {}".format(best_sum.sum, best_sum.len, best_sum.ratio))
    print("best ration {} with a sum of {} and {} results".format(best_sum_ratio.ratio, best_sum_ratio.sum, best_sum_ratio.len))
