# this is a good solution with a search speed of O(1)
# but has the slowest insert speed
def find_first_recurring_char_with_a_dict(string):
    count = {}
    for char in string:
        if char in count:
            return char
        # changed after looking at what
        # is the cheapest empty value for a key
        count[char] = None


# this solution holds the best insert speed
# but the worst search speed of O(n)
# that being said, from looking at our stress test:
#   find_first_recurring_char_with_a_dict(32) average time:  7.935303908128005e-07
#   find_first_recurring_char_with_a_list(32) average time:  3.747866703913762e-07
#   find_first_recurring_char_with_a_set(32) average time:  4.0375636174128606e-07
#   find_first_recurring_char_with_a_dict(255) average time:  8.839313800518329e-07
#   find_first_recurring_char_with_a_list(255) average time:  4.4326048630934493e-07
#   find_first_recurring_char_with_a_set(255) average time:  5.427250495323768e-07
#   find_first_recurring_char_with_a_dict(16000) average time:  5.483731627464294e-07
#   find_first_recurring_char_with_a_list(16000) average time:  1.1622950434684753e-06
#   find_first_recurring_char_with_a_set(16000) average time:  7.895752787590026e-07
#   find_first_recurring_char_with_a_dict(65000) average time:  4.835832118988037e-07
#   find_first_recurring_char_with_a_list(65000) average time:  6.312894821166992e-07
#   find_first_recurring_char_with_a_set(65000) average time:  9.524834156036377e-07
#   find_first_recurring_char_with_a_dict(2000000) average time:  9.270298480987549e-07
#   find_first_recurring_char_with_a_list(2000000) average time:  8.631134033203125e-07
#   find_first_recurring_char_with_a_set(2000000) average time:  7.250785827636719e-07
# we can see that for most cases a list approach is the best since the search time is negligible
def find_first_recurring_char_with_a_list(s: str) -> str:
    r = []
    for c in s:
        if c in r:
            return c
        r.append(c)


# this is overall the best solution for performance
# with a search speed of O(1)
# and a faster insert speed than a dict
def find_first_recurring_char_with_a_set(s: str) -> str:
    r = set()
    for c in s:
        if c in r:
            return c
        r.add(c)


if __name__ == "__main__":
    print(find_first_recurring_char_with_a_list("abcdabcd"))
    print(find_first_recurring_char_with_a_list("abcd"))
    print(find_first_recurring_char_with_a_set("abcdabcd"))
    print(find_first_recurring_char_with_a_set("abcd"))
    print(find_first_recurring_char_with_a_dict("abcdabcd"))
    print(find_first_recurring_char_with_a_dict("abcd"))

    from time import time

    t1 = time()

    l1 = ["a" for _ in range(1000000)]
    l1.append("barbiqu")
    l1 = l1 + ["a" for _ in range(1000000)]
    s1 = "".join(l1)
    d1 = {"a": None, "barbiqu": None}
    set1 = {"a", "barbiqu"}

    t2 = time()
    print(t2-t1, "created l1 & s1")

    # string is O(1)

    t1 = time()
    if "barbiqu" in s1:
        t2 = time()
        print(t2 - t1, "arbiqu in s1")

    t1 = time()
    if "barbiqub" in s1:
        raise Exception("error")
    else:
        t2 = time()
        print(t2 - t1, "barbiqub not in s1")

    t1 = time()
    if "barbiqub" not in s1:
        t2 = time()
        print(t2 - t1, "barbiqub not in s1")

    # list is O(n)

    t1 = time()
    if "barbiqu" in l1:
        t2 = time()
        print(t2 - t1, "arbiqu in l1")

    t1 = time()
    if "barbiqub" in l1:
        raise Exception("error")
    else:
        t2 = time()
        print(t2 - t1, "barbiqub not in l1")

    t1 = time()
    if "barbiqub" not in l1:
        t2 = time()
        print(t2 - t1, "barbiqub not in l1")

    # dict is O(1)

    t1 = time()
    if "barbiqu" in d1:
        t2 = time()
        print(t2 - t1, "arbiqu in d1")

    t1 = time()
    if "barbiqub" in d1:
        raise Exception("error")
    else:
        t2 = time()
        print(t2 - t1, "barbiqub not in d1")

    t1 = time()
    if "barbiqub" not in d1:
        t2 = time()
        print(t2 - t1, "barbiqub not in d1")

    # set is O(1)

    t1 = time()
    if "barbiqu" in set1:
        t2 = time()
        print(t2 - t1, "arbiqu in set1")

    t1 = time()
    if "barbiqub" in set1:
        raise Exception("error")
    else:
        t2 = time()
        print(t2 - t1, "barbiqub not in set1")

    t1 = time()
    if "barbiqub" not in set1:
        t2 = time()
        print(t2 - t1, "barbiqub not in set1")

    # what is the cheapest empty value for a key
    print(None.__sizeof__())
    print((1).__sizeof__())
    print("".__sizeof__())
    print(True.__sizeof__())
    print(None is None)

    # who has the fastest insert
    data = [f"{i}" for i in range(2000000)]

    t1 = time()
    l1 = []
    for i in data:
        l1.append(i)
    t2 = time()
    print(t2 - t1, "l1 insert time")

    t1 = time()
    d1 = {}
    for i in data:
        d1[i] = None
    t2 = time()
    print(t2 - t1, "d1 insert time")

    t1 = time()
    s1 = "".join(l1)
    t2 = time()
    print(t2 - t1, "s1 insert time")

    t1 = time()
    set1 = set()
    for i in data:
        set1.add(i)
    t2 = time()
    print(t2 - t1, "set1 insert time")

    # stress test
    import random

    max_values = [32, 255, 16000, 65000, 2000000, 20000000]

    results = {
        "find_first_recurring_char_with_a_dict": {
            # [max_value]: average_time
        },
        "find_first_recurring_char_with_a_list": {
            # [max_value]: average_time
        },
        "find_first_recurring_char_with_a_set": {
            # [max_value]: average_time
        },
    }

    for max_value in max_values:
        iterations = max_value * 10

        if iterations > 200000:
            iterations = 200000

        elif iterations < 65000:
            iterations = 65000

        results["find_first_recurring_char_with_a_dict"][max_value] = 0
        results["find_first_recurring_char_with_a_list"][max_value] = 0
        results["find_first_recurring_char_with_a_set"][max_value] = 0

        for iteration in range(iterations):
            l = set()
            for _ in range(max_value):
                i = str(random.randrange(0, max_value))
                if i in l:
                    break
                l.add(i)
            s = "".join(l)

            t1 = time()
            find_first_recurring_char_with_a_dict(s)
            t2 = time()
            results["find_first_recurring_char_with_a_dict"][max_value] += t2 - t1

            t1 = time()
            find_first_recurring_char_with_a_list(s)
            t2 = time()
            results["find_first_recurring_char_with_a_list"][max_value] += t2 - t1

            t1 = time()
            find_first_recurring_char_with_a_set(s)
            t2 = time()
            results["find_first_recurring_char_with_a_set"][max_value] += t2 - t1

        results["find_first_recurring_char_with_a_dict"][max_value] = results["find_first_recurring_char_with_a_dict"][max_value]/iterations
        results["find_first_recurring_char_with_a_list"][max_value] = results["find_first_recurring_char_with_a_list"][max_value]/iterations
        results["find_first_recurring_char_with_a_set"][max_value] = results["find_first_recurring_char_with_a_set"][max_value]/iterations
        print(f"find_first_recurring_char_with_a_dict({max_value}) average time: ", results["find_first_recurring_char_with_a_dict"][max_value])
        print(f"find_first_recurring_char_with_a_list({max_value}) average time: ", results["find_first_recurring_char_with_a_list"][max_value])
        print(f"find_first_recurring_char_with_a_set({max_value}) average time: ", results["find_first_recurring_char_with_a_set"][max_value])

    print("results", results)
