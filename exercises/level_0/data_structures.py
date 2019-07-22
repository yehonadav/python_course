# import random
# from exercises.data import get_data
# users = get_data(5)
#
#
# # print users type
# print(type(users))
#
# # get the first user
# user = users[0]
#
# # print its type
# print(type(user))
#
# # view users
# for user in users:
#     print(user)
#
# # view the second user
# print(users[1])
#
# names = []
# for user in users:
#     names.append(user['name'])
#
# names1 = []
# for user in users:
#     names1.append(user['name'])
#
# i = 0
# names2 = []
# while i < len(users):
#     i += 1
#     names2.append(user['name'])
#
# names3 = [user['name'] for user in users]
# names4 = {user['name'] for user in users}
# names5 = {user['name']: len(user['name']) for user in users}
# names6 = (user['name'] for user in users)
#
# names7 = []
# for user in users:
#     if len(user['name']) < 10:
#         names7.append(user['name'])
#
# i = 0
# names8 = []
# while i < len(users):
#     i += 1
#     if len(user['name']) < 10:
#         names8.append(user['name'])
#
# names9 = [user['name'] for user in users if len(user['name']) < 10]
# names10 = {user['name'] for user in users if len(user['name']) < 10}
# names11 = {user['name']: len(user['name']) for user in users if len(user['name']) < 10}
# names12 = (user['name'] for user in users if len(user['name']) < 10)
#
# # view names
# print(names)
#
# # print names length
# print(len(names))
#
# # get the first name
# first_name = names[0]
#
# # get the last name
# last_name = names[-1]
#
# # get all names excluding first and last
# new_names = names[1:-1]
# print(new_names)
#
# # get names 0, 2, 4 ...
# evens = names[::2]
#
# # get names 1, 3, 5 ...
# odds = names[1::2]
#
# # print the first name as upper case!
# print(first_name.upper())
#
# # print the first name as lower case!
# print(first_name.lower())
#
# # get the first and last characters of each name from names
# lis1 = []
# for name in names:
#     lis1.append(name[0] + name[-1])
#
# # sort the result
# lis1.sort()
#
# # replace all characters with upper case characters
# for i in range(len(lis1)):
#     lis1[i] = lis1[i].upper()
#
# # translate characters to numbers
# translate = {
#     'A': 0,
#     'B': 1,
#     'C': 2,
#     'D': 3,
#     'E': 4,
#     'F': 5,
#     'G': 6,
#     'H': 7,
#     'I': 8,
#     'J': 9,
#     'K': 10,
#     'L': 11,
#     'M': 12,
#     'N': 13,
#     'O': 14,
#     'P': 15,
#     'Q': 16,
#     'R': 17,
#     'S': 18,
#     'T': 19,
#     'U': 20,
#     'V': 21,
#     'W': 22,
#     'X': 23,
#     'Y': 24,
#     'Z': 25,
# }
# print(lis1)
# for i, item in enumerate(lis1):
#     lis1[i] = translate[item[0]] + translate[item[1]]
# print(lis1)
#
# # translate strings to numbers
# for i, value in enumerate(lis1):
#     lis1[i] = int(value)
#
# # sort the numbers
# lis1.sort()
# print(lis1)
#
# # sort in reverse
# lis1.sort(reverse=True)
# print(lis1)
#
# # get a random user from users
# random_user = random.choice(users)
#
# # get the user address
# address = random_user['address']
#
# # find 'A', 'B', 'c', 'd' first indexes in the address, why -1 might get printed?
# print('index A:', address.find('A'))
# print('index B:', address.find('B'))
# print('index c:', address.find('c'))
# print('index d:', address.find('d'))
#
# # count all occurrences of 'A', 'B', 'c', 'd' in the address
# print('occurrences of A', address.count('A'))
# print('occurrences of B', address.count('B'))
# print('occurrences of c', address.count('c'))
# print('occurrences of d', address.count('d'))
#
# # get all user ages
# ages = [user['age'] for user in users]
# # ages = []
# # for user in users:
# #     ages.append(user['age'])
#
# # find the average age
# print('average age', sum(ages)/len(ages))
# # summ = 0
# # for age in ages:
# #     summ += age
# # avg = summ/len(ages)
#
# # find the middle(index wise) age
# print('middle(index wise) age', ages[int(len(ages)/2)])
#
# # find the smallest age before sorting
# print('smallest age', min(ages))
#
# # find the biggest age before sorting
# print('biggest age', max(ages))
#
# ages.sort()
#
# # find the smallest age after sorting
# print('smallest age', ages[0])
#
# # find the biggest age after sorting
# print('smallest age', ages[-1])
#
# # find the middle sorted age
# print('middle sorted age', ages[int(len(ages)/2)])
#
# # multiply users by 3
# users = users * 3
#
# # check if 2 users share the same email address
# emails = []
# for user in users:
#     if user['email'] in emails:
#         print(f'email {user["email"]} encountered twice!')
#         break
#     emails.append(user["email"])
#
#
#
# # generator comprehension
# ages = (user['age'] for user in users)
# print(ages)
# for age in ages:
#     print(age)

print(dir(1))