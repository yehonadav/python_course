import json
import datetime
from exercises.level_1.file_exercises.json_phone_book import filename, get_phone_book

current_year = datetime.datetime.now().year

menu = """

========== Json Phone Book ==========

       Please select an option

(1) add user to phone book
(2) delete user from phone book
(3) search user in phone book
(4) view all users in the phone book
(0) quit

"""
options = '01234'
choice = '0'
while choice in options:
    try:
        choice = input(menu)

        if choice not in options:
            print(f'{choice} is an invalid option, try again')
            choice = '0'
            continue

        if choice == '1':
            new_user = {
                'name': input('enter user name:'),
                'address': input('enter user address:'),
                'age': int(input('enter user age:')),
                'birth': int(input('enter user birth:')),
                'phone_number': input('enter user phone number:'),
            }
            if not 0 <= new_user['age'] <= 120:
                raise ValueError("invalid user age, age range: 0-120")
            if not current_year - 120 <= new_user['birth'] <= current_year:
                raise ValueError(f"invalid user birth, birth range: {current_year - 120}-{current_year}")

            users = get_phone_book()

            duplicate = False
            for user in users:
                if user['name'] == new_user['name'] \
                and user['address'] == new_user['address'] \
                or user['phone_number'] == new_user['phone_number']:
                    duplicate = True
                    break

            if duplicate:
                print(f'user {new_user["name"]} with address {new_user["address"]} and phone {new_user["phone_number"]} already exist')
            else:
                users.append(new_user)
                with open(filename, 'w') as phone_book:
                    json.dump(users, phone_book)
                print(f'user {new_user["name"]} added successfully')

        elif choice == '2':
            delete = input('delete users by name, address or phone number:')
            users = get_phone_book()
            update = [
                user
                for user in users
                if user['name'] != delete
                and user['phone_number'] != delete
                and user['address'] != delete
            ]
            if len(update) == len(users):
                print(f'{delete} not found in {filename}')
            else:
                with open(filename, 'w') as phone_book:
                    json.dump(update, phone_book)
                print(f'deleted users with {delete} successfully')

        elif choice == '3':
            find = input('find users by name, age, birth, address or phone number:')
            if find.isnumeric():
                find = int(find)
            users = get_phone_book()

            search = [user for user in users if find in user.values()]
            if search:
                print(f'found {len(search)} users:')
                for result in search:
                    print(' ', result)
            else:
                print(f'users with {find} not dound')

        elif choice == '4':
            users = get_phone_book()
            print('========== Json Phone Book ==========\n')
            print(f'found {len(users)} results:')
            for user in users:
                print('  ', user)

        else:
            print('goodby =)')
            break

    except Exception as e:
        print('oops, something went wrong', e)
