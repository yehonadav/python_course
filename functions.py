def compute(*numbers):
    sum1 = 0.0
    for number in numbers:
        sum1 += number

    sum2 = sum1
    for i in str(sum1).split():
        sum2 *= float(i)

    sum = (sum2**numbers[0]) * (2 + sum1 + 1/sum2)
    return sum


def enlarge_sequence(sequence, size=100):
    for i in sequence:
        sequence.append(compute(*sequence))
        if len(sequence) > size:
            break

    for i in sequence:
        print(i)


sequence = [0.1, 0.3, 0.7, 1, 2]
enlarge_sequence(sequence, size=12)


sequence = [0.1, 0.3, 0.7, 1, 2]
for i in sequence:
    sum1 = 0.0
    for number in sequence:
        sum1 += number

    sum2 = sum1
    for i in str(sum1).split():
        sum2 *= float(i)

    sum = (sum2**sequence[0]) * (2 + sum1 + 1/sum2)
    sequence.append(sum)
    break

for i in sequence:
    sum1 = 0.0
    for number in sequence:
        sum1 += number

    sum2 = sum1
    for i in str(sum1).split():
        sum2 *= float(i)

    sum = (sum2**sequence[0]) * (2 + sum1 + 1/sum2)
    sequence.append(sum)
    break

for i in sequence:
    print(i)