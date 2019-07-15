# file_content = """
# # # # import datetime
# # # #
# # # #
# # # # if __name__ == '__main__':
# # # #     name = input("Enter your name: ")
# # # #     age = int(input("Enter your age: "))
# # # #     birth = datetime.datetime.utcnow().year - age
# # # #     print("{}; you were born in {}".format(name, birth))
# # # num = 50
# # # print(type(num))
# # # print(type(float(num)))
# # # print(type(str(float(num))))
# # # print(type('12345'.split('@')))
# # #
# # # mylist = '12#3#45'.split('#')
# # # print(mylist)
# # # print(mylist[:2])
# # # print('robinson'.upper().lower())
# #
# # # # print your age using input function
# # # age = input('enter your age:')
# # # print(age)
# # #
# # # # print your age*2 using input
# # # age = input('enter your age, it will double:')
# # # print(int(age)*2)
# # #
# # # # print your age*2 using input
# # # age = input('enter your age, it will be powered:')
# # # print(int(age)**2)
# #
# # # print your birth year and month using input
# # # print(type(age) is str)
# # birth_year_and_month = input('enter your birth year, and month:')
# # print(birth_year_and_month)
# #
# # # using input, get your birth year and month, print your age
# # current_year = 2019
# # current_month = 7
# # birth_year_and_month = input('enter your birth year, and month:')
# # # birth_year_and_month = birth_year_and_month.split(' ')
# # # year = int(birth_year_and_month[0])
# # # month = int(birth_year_and_month[1])
# # year = int(birth_year_and_month[:4])
# # month = int(birth_year_and_month[5:])
# # my_age = current_year - year
# # print(my_age)
# #
# # current_date = current_year + current_month/12
# # birth_date = year + month/12
# # my_age = current_date - birth_date
# # print(my_age)
# import random
#
# guess_me = random.randint(0, 4)
# my_guess = input('guess a number between 0-4')
# guess1 = str(guess_me) == my_guess
# print(guess1)
#
# # if the guess is wrong twice, print the correct answer
# my_guess = input('guess a number between 0-4')
# guess2 = str(guess_me) == my_guess
# print(guess2)
#
# if guess1 is False and guess2 is False:
#     print(f'correct answer is: {guess_me}')
#     print('correct answer is: ' + str(guess_me))
# """
# # please stringify all the content in your file to this point.
#
# # print the number of occurrences of the character 'a'
# print('a', file_content.count('a'))
# print('b', file_content.count('b'))
# print('c', file_content.count('c'))
# print('i', file_content.count('i'))
#
# # find all words as size or as a list in the file
# file_content = file_content.replace('\n', ' ')
# file_content = file_content.replace('\t', ' ')
# words = file_content.split(' ')
#
# # words = filter(lambda word: not word.isnumeric(), words)
# print(len(words))
#
#
# first = words[0]
# last = words[-1]
# middle = words[int(len(words)/2)]
# if first.find('0') and first.find('1') and first.find('2') \
# and first.find('3') and first.find('4') and first.find('5') \
# and first.find('6') and first.find('7') and first.find('8') \
# and first.find('9'):
#     print('the first word is really a word')
#
# numbers = '0123456789'
# for number in numbers:
#     if number in middle:
#         print('not a word')
#         break
# else:
#     print('middle is a word')
#
#
#
# back_to_string = ''.join(words)
# print(type(back_to_string))

def combo(a, b):
    return a + b


yummy_fruits = ('apple', 'banana', 'cherry')
sour_fruits = ('orange', 'lemon', 'pineapple')


def exercise96():
    def calc(n): return len(n) * sum(range(1, len(n) + 1))
    ai = ['6.', '40.0', '75.00', '126.00']
    res = map(calc, ai)
    print(sum(res))


def exercise97():
    names = ['Tom', 'Gon', 'Don', 'Bon']
    low = map(lambda name: name.lower(), names)
    hig = map(lambda name: name.upper(), names)
    print(*low, *hig)


def exercise98():
    from exercises.data import get_data
    users = get_data(10)
    names = map(lambda user: user['name'], users)
    print((*names,))


def exercise99():
    comb_fruits = map(combo, yummy_fruits, sour_fruits)
    print(*comb_fruits)


def exercise100():
    f1 = filter(lambda fruit: 'a' in fruit, yummy_fruits)
    f2 = filter(lambda fruit: fruit.startswith('o') or fruit.endswith('le'), sour_fruits)
    print('filtered fruits', *f1, *f2)


def exercise101():
    from exercises.data import get_data
    from exercises.helpers import random_range
    import random
    users = get_data(1000)
    for _ in random_range(3, 30):
        suspect1 = users[random.randint(0, 999)]
        suspect2 = users[random.randint(0, 999)]
        suspect1['email'] = suspect2['email']
        print(suspect1['email'])

    # lean users
    users = tuple(map(lambda user: {
            'name': user['name'],
            'age': user['age'],
            'address': user['address'],
            'phone_number': user['phone_number'],
            'email': user['email']
        }, users))

    # find suspects
    counter = {}
    fraud_suspects = {}
    for user in users:
        if user['email'] in counter:
            if user['email'] not in fraud_suspects:
                fraud_suspects[user['email']] = [user, counter[user['email']]]
            else:
                fraud_suspects[user['email']].append(user)
        else:
            counter[user['email']] = user

    # print suspects
    for email in fraud_suspects:
        suspects = map(lambda user: {
            'name': user['name'],
            'address': user['address'],
            'phone_number': user['phone_number'],
        }, fraud_suspects[email])
        print(f'users with email {email} are suspects to fraud:')
        for suspect in suspects:
            print(f'\t{suspect}')
        print('\n')

    # get age groups
    young = filter(lambda user: user['age'] < 19, users)
    grown = filter(lambda user: 18 < user['age'] < 40, users)
    old = filter(lambda user: 39 < user['age'], users)

    # list all suspects
    all_suspects = []
    for suspects in fraud_suspects.values():
        for suspect in suspects:
            if suspect not in all_suspects:
                all_suspects.append(suspect)

    # get age group suspects
    young_suspects = filter(lambda user: user['age'] < 19, all_suspects)
    grown_suspects = filter(lambda user: 18 < user['age'] < 40, all_suspects)
    old_suspects = filter(lambda user: 39 < user['age'], all_suspects)

    # calculate age group fraud susceptibility
    young = tuple(young)
    grown = tuple(grown)
    old = tuple(old)
    susceptibility = [
        ['young', len(tuple(young_suspects))],
        ['grown', len(tuple(grown_suspects))],
        ['old', len(tuple(old_suspects))]
    ]
    if len(young) == 0:
        susceptibility[0][1] = '0%'
    else:
        susceptibility[0][1] = f'{round(100*susceptibility[0][1]/len(young), 2)}%'
    if len(grown) == 0:
        susceptibility[1][1] = '0%'
    else:
        susceptibility[1][1] = f'{round(100*susceptibility[1][1]/len(grown), 2)}%'
    if len(old) == 0:
        susceptibility[2][1] = '0%'
    else:
        susceptibility[2][1] = f'{round(100*susceptibility[2][1]/len(old), 2)}%'

    susceptibility.sort(key=lambda group: group[1], reverse=True)
    print('groups susceptible to fraud are ordered from most to least susceptible in percentage:')
    print(*susceptibility)



if __name__ == '__main__':
    exercise96()
    exercise97()
    exercise98()
    exercise99()
    exercise100()
    exercise101()
