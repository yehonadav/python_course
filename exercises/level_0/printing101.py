# print your name
print("jonny")

# use concat to print your name and age (don't forget to space)
print("jonny " + "27")

# print 3 numbers separated by tabs
print("1\t2\t3")

# print 3 numbers separated by newlines
print("1\n2\n3\n")

# get 4 numbers using input and print their sum
num1 = input('please select number1:')
num2 = input('please select number2:')
num3 = input('please select number3:')
num4 = input('please select number4:')
print(num1+num2+num3+num4)

# print the 4 numbers sum as integers
print(int(num1)+int(num2)+int(num3)+int(num4))

# get 3 numbers using input
num1 = input('please select number1:')
num2 = input('please select number2:')
num3 = input('please select number3:')

# print the sum of the first 2 divided by the third
computation = (float(num1)+float(num2))/float(num3)
print(computation)

# print a rounded result with no more than 2 characters after the dot (3.333333 -> 3.33)
print(round(computation, 2))

# get 2 numbers using input
num1 = input('please select number1:')
num2 = input('please select number2:')

# print how many times the second number consumes the first
print(float(num1) // float(num2))

# print the leftover
print(float(num1) % float(num2))

# a storage room of 4x4x3
# create a function to insert/pop items with their size
# and to calculate how much room is available
# create a function to receive a radius and print its circumference, round the result to x.xx
#