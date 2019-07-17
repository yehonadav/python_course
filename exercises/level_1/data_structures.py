from exercises.data import get_data
users = get_data(5)


# print users type
print(type(users))

# get the first user
user = users[0]

# print its type
print(type(user))

# view users
for user in users:
    print(user)

# view the second user
print(users[1])

names = []
for user in users:
    names.append(user['name'])

# view names
print(names)

# print names length
print(len(names))

# get the first name
first_name = names[0]

# get the last name
last_name = names[-1]

# get all names excluding first and last
new_names = names[1:-1]
print(new_names)

# get names 0, 2, 4 ...
evens = names[::2]

# get names 1, 3, 5 ...
odds = names[1::2]

# print the first name as upper case!
print(first_name.upper())

# print the first name as lower case!
print(first_name.lower())

# get the first and last characters of each name from names
lis1 = []
for name in names:
    lis1.append(name[0] + name[-1])

# sort the result
lis1.sort()

# replace all characters with upper case characters
for i in range(len(lis1)):
    lis1[i] = lis1[i].upper()

# translate characters to numbers
translate = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
}
print(lis1)
for i, item in enumerate(lis1):
    lis1[i] = translate[item[0]] + translate[item[1]]
print(lis1)

# translate strings to numbers
for i, value in enumerate(lis1):
    lis1[i] = int(value)

# sort the numbers
lis1.sort()
print(lis1)

# sort in reverse
lis1.sort(reverse=True)
print(lis1)

# get a random user from users
import random
random_user = random.choice(users)

# get the user address
address = random_user['address']

# find 'A', 'B', 'c', 'd' first indexes in the address, why -1 might get printed?
print('index A:', address.find('A'))
print('index B:', address.find('B'))
print('index c:', address.find('c'))
print('index d:', address.find('d'))

# count all occurrences of 'A', 'B', 'c', 'd' in the address
print('occurrences of A', address.count('A'))
print('occurrences of B', address.count('B'))
print('occurrences of c', address.count('c'))
print('occurrences of d', address.count('d'))

# get all user ages
ages = [user['age'] for user in users]
# ages = []
# for user in users:
#     ages.append(user['age'])

# find the average age
print('average age', sum(ages)/len(ages))
# summ = 0
# for age in ages:
#     summ += age
# avg = summ/len(ages)

# find the middle(index wise) age
print('middle(index wise) age', ages[int(len(ages)/2)])

# find the smallest age before sorting
print('smallest age', min(ages))

# find the biggest age before sorting
print('biggest age', max(ages))

ages.sort()

# find the smallest age after sorting
print('smallest age', ages[0])

# find the biggest age after sorting
print('smallest age', ages[-1])

# find the middle sorted age
print('middle sorted age', ages[int(len(ages)/2)])

# multiply users by 3
users = users * 3

# check if 2 users share the same email address

# create a mygame1.py file
# print this message: 'welcome to my game'
# create a while loop
# use the input function to print a menu like so:
# (1) new game
# (2) try again
# (3) quit
# if the user input is not 1,2 or 3 print an error message
# if the user pressed 3 break the loop
# if the user press 1 activate a play function
# if the user press 2 activate a replay function
# create a play function
#   create a number between 1-10
#   save the number in a dictionary outside the function
#   loop 3 times
#       ask the user to guess the number
#       if the answer is correct, print a message and return
#       if the loop ended print a lose message and return
# create a replay function that takes the random number from the dictionary
# and use it to replay

# create a simple_as_py.py file
# print your name
# use concat to print your name and age (don't forget to space)
# print 3 numbers separated by tabs
# print 3 numbers separated by newlines
# get 4 numbers using input and print their sum
#   print the sum as integer
# get 3 numbers using input
#   print the sum of the first 2 divided by the third
#   print a rounded result with no more than 2 characters after the dot (3.333333 -> 3.33)
# get 2 numbers using input
#   print how many times the second number consumes the first
#   print the leftover
# a storage room of 4x4x3
#   create a pfunction to insert/pop items with their size
#   and to calculate how much room is available
# create a function to receive a radius and print its circumference, round the result to x.xx

