from exercises.data import get_data
import json
import os

users_filename = 'users.json'
users = [
    {
        "name": "Kathleen Davis",
        "address": "1392 Washington Drive\nWest Jameston, AK 27438",
        "age": 29,
        "birth": 1967,
        "automotive_number": "547 4RN",
        "phone_number": "001-382-701-1411x1446",
        "bank_account": "GB04BSDB1627449867830",
        "favorite_color": "white",
        "company": "Patel-Morgan",
        "catch_phrase": "Down-sized uniform structure",
        "email": "zgarcia@hotmail.com"
    }
]

if not os.path.exists(users_filename):
    with open(users_filename, 'w') as f:
        json.dump(users, f)

with open('users.json') as f:
    old_users = json.load(f)

new_users = get_data(5)

with open('users.json', 'w') as f:
    json.dump(old_users + new_users, f, indent=2)