import time
from exercises.data import get_data
from exercises.level_1.hobbies import add_random_hobby, add_second_hobby, hobbies, hobbies2


def get_addresses(users, start=0, stop=50):
    return [users[i]['address'] for i in range(start, stop)]


def count_address_numbers(user_addresses):
    address_number = user_addresses[0].split(' ', 1)[0]
    counter = {address_number: 0}
    most_counted_address_number = address_number

    for address in user_addresses:
        address_number = address.split(' ', 1)[0]
        if not address_number.isnumeric():
            continue
        if address_number in counter:
            counter[address_number] += 1
            if counter[address_number] > counter[most_counted_address_number]:
                most_counted_address_number = address_number
        else:
            counter[address_number] = 1
    print(f'most counted address number is \'{most_counted_address_number}\', counted {counter[most_counted_address_number]} times')


def encounter_name_twice(users):
    counter = {}
    i = 0
    while i < len(users):
        if users[i]['name'] not in counter:
            counter[users[i]['name']] = 1
        else:
            print(f'the name {users[i]["name"]} has been encountered twice!')
            return
        i += 1


def sum_index10(users):
    age_sum = 0
    for i, user in enumerate(users):
        age_sum += user['age']
        if age_sum >= (i+1)*10:
            print('users age summary:', age_sum, i)
            return


def name_and_address20(users):
    for user in users:
        if len(user['name']) + len(user['address']) > 20:
            print(f'found user with a combined name+address length bigger than 20 characters: {user["name"]} {user["address"]}')
            return


def assert_names(users):
    for user in users:
        assert 2 <= len(user['name']) <= 20


def assert_ages(users):
    for user in users:
        assert 0 <= user['age'] <= 120


def assert_user_hobby(users):
    all_hobbies = hobbies + hobbies2

    for user in users:
        assert user['hobby'] in all_hobbies
        assert user['second hobby'] in all_hobbies


def get_user_uptime(user):
    created = user['created']
    timestamp = time.time()
    uptime = timestamp - created
    return uptime


def print_users_avg_uptime(users):
    avg_uptime = []
    for user in users:
        timestamp = time.time()
        try:
            avg_uptime.append(get_user_uptime(user))
        except KeyError:
            user['created'] = timestamp
            avg_uptime.append(get_user_uptime(user))
    print(f'users average uptime: {sum(avg_uptime)}')


def find_equal_neighbor_age(users):
    age = None
    for i, user in enumerate(users):
        if age == user['age']:
            print(f'found neighboring users \'{user["name"]}\' & \'{users[i-1]["name"]}\' with equal age {age}')
            return
        age = user['age']


def create_more_users(users):
    initial_users_size = len(users)
    timestamp = time.time()
    while time.time() - timestamp < 2:
        user_set = get_data(10)
        for user in user_set:
            users.append(user)
    print(f'created {len(users)-initial_users_size} new users')


if __name__ == '__main__':
    users = get_data(2000)

    user_addresses = get_addresses(users)

    count_address_numbers(user_addresses)

    encounter_name_twice(users)

    sum_index10(users)

    name_and_address20(users)

    try:
        assert_names(users)
    except AssertionError:
        print('found user with invalid name')

    try:
        assert_ages(users)
    except AssertionError:
        print('found user with invalid age')

    add_random_hobby(users)
    add_second_hobby(users)
    users[5]['hobby'] = 'qwedrfghjhgfds'
    try:
        assert_user_hobby(users)
    except AssertionError:
        print('found user with invalid hobby')
    else:
        raise Exception('expectation failed: expected to find a user with an invalid hobby')

    print_users_avg_uptime(users)

    find_equal_neighbor_age(users)

    create_more_users(users)
