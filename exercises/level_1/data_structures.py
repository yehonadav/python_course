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
for i, value in enumerate(lis1):
    lis1[i] = translate[lis1[i][0]] + translate[lis1[i][1]]
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

