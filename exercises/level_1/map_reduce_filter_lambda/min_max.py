from exercises.data import get_data

users = get_data(15)

# get the max age with lambda
print(f'max age {max(users, key=lambda user: user["age"])["age"]}')

# get the min age with lambda
print(f'min age {min(users, key=lambda user: user["age"])["age"]}')

# get the max age with for loop
age = users[0]['age']
for user in users:
    if user['age'] > age:
        age = user['age']
print(f'max age {age}')

# get the min age with for loop
age = users[0]['age']
for user in users:
    if user['age'] < age:
        age = user['age']
print(f'min age {age}')
