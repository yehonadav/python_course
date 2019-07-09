from exercises.data import get_data
from statistics import median
import random


hobbies = [
    'football',
    'strongman',
    'mario',
    'tekken-3',
    'beach',
    'soccer',
    'bacon',
    'pool',
    'dodge ball'
]

hobbies2 = [
    'star wars',
    'star trek',
    'mario cart',
    'draw',
    'manga artist',
    'ogre slayer',
    'porn star',
    'high five guy!',
    'idan hakimi'
]


def measure_users_average_age(users):
    sum = 0
    for user in users:
        sum += user['age']
    avg = sum/len(users)
    print(f'users average age is {avg}')


def find_most_common_user_name(users):
    initial_user = users[0]
    common = {initial_user['name']: 0}
    most_common = initial_user['name']

    for user in users:
        if user['name'] in common:
            common[user['name']] += 1
        else:
            common[user['name']] = 1
        if common[user['name']] > common[most_common]:
            most_common = user['name']
    print(f'most common user name is \'{most_common}\', counted {common[most_common]} times')


def measure_users_median_age(users):
    print(f'users median age is {median([user["age"] for user in users])}')


def add_random_hobby(users):
    for user in users:
        user['hobby'] = random.choice(hobbies)


def count_hobbies(users):
    count = {hobby: 0 for hobby in hobbies}
    for user in users:
        count[user['hobby']] += 1
    for hobby in count:
        print(hobby, count[hobby])


def add_second_hobby(users):
    for user in users:
        user['second hobby'] = random.choice(hobbies)
        if user['second hobby'] == user['hobby']:
            if random.randint(0, 2):
                user['second hobby'] = random.choice(hobbies2)
            else:
                user['hobby'] = random.choice(hobbies2)


def count_hobbies2(users):
    count = {hobby: 0 for hobby in hobbies2}
    for user in users:
        if user['hobby'] in hobbies2:
            count[user['hobby']] += 1
        elif user['second hobby'] in hobbies2:
            count[user['second hobby']] += 1

    for hobby in count:
        print(hobby, count[hobby])


if __name__ == '__main__':
    users = get_data(2000)

    measure_users_average_age(users)
    find_most_common_user_name(users)
    measure_users_median_age(users)

    add_random_hobby(users)
    count_hobbies(users)
    add_second_hobby(users)
    print('\n\n\n\n\n')
    count_hobbies2(users)
