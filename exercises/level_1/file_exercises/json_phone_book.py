import os
import json
from exercises.data import get_data


filename = 'phone_book.json'


def get_phone_book(new_users=None):
    if not os.path.exists(filename):
        print(f'creating {filename}')
        users = []
        with open(filename, 'w') as phone_book:
            json.dump(users, phone_book)
    else:
        print(f'getting users from {filename}')
        with open(filename) as phone_book:
            users = json.load(phone_book)

    if new_users:
        users.extend(new_users)
        print(f'saving users in {filename}')
        with open(filename, 'w') as phone_book:
            json.dump(users, phone_book, indent=2)
    return users


if __name__ == "__main__":
    print('creating 5 users...')
    users = [
        {
            'name': user['name'],
            'address': user['address'],
            'age': user['age'],
            'birth': user['birth'],
            'phone_number': user['phone_number']
        }
        for user in get_data(5)
    ]

    users = get_phone_book(new_users=users)

    print('getting users name, age, phone_number')
    users = sorted([
        {
            'name': user['name'],
            'age': user['age'],
            'phone_number': user['phone_number'],
        }
        for user in users
    ], key=lambda user: user['age'])

    print('\nusers sorted by age:')
    for user in users:
        print(f'  {user["name"]}, {user["phone_number"]}')
