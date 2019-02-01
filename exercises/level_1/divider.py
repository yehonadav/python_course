number = int(input('Enter a number:'))
print(list(filter(lambda x: number % x == 0, range(1, number))))
