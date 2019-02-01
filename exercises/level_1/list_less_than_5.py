ages = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

if __name__ == "__main__":
    less_than_5 = []
    for age in ages:
        if age < 5:
            less_than_5.append(age)
    for age in less_than_5:
        print(age)
