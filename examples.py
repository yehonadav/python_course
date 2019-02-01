# # from exercises.data import get_data
# #
# # data = get_data(20)
# #
# #
# # for person in data:
# #     if person['age'] < 13:
# #         for k in person:
# #             print(k, person[k])
# #         break
# # else:
# #     print('all old people')
# #
#
#
# def get_fib_sum(sum):
#     f = []
#     n_minus_1 = 0
#     n = 1
#     while n < sum:
#         f.append(n_minus_1)
#         n, n_minus_1 = n_minus_1 + n, n
#     return f
#
#
# print(sum(get_fib_sum(21)))


# def get_arg(name, age: int, hobby, *optional_hobbies, **other):
#     # enforce type
#     if not isinstance(age, int):
#         raise TypeError
#
#     # handle optional hobbies
#     oh = ''
#     for i in optional_hobbies:
#         oh += ' & ' + i
#
#     # handle other content
#     oth = ''
#     for i in other:
#         oth += ' {} {}'.format(i, other[i])
#
#     sentance = "my name is {}, {}.\nI like to {}{}.{}".format(name, age, hobby, oh, oth)
#     return sentance
#
#
# print(get_arg('gob', 30, 'fly', 'snow board', 'porn', wood='i like to chop'))

# תכתוב תוכנית אשר מקבלת מידע מתוך exercises.data get_data
# וממיינת את השמות לרשימה בסדר לפי הabc
# יש להוסיף לרשימה את כתובת המגורים של האנשים


def sort_names_with_addresses(data):
    names = []
    names_and_addresses = {}
    for person in data:
        if person['name'] in names:
            names_and_addresses[person['name']].append(person['address'])
        else:
            names.append(person['name'])
            names_and_addresses[person['name']] = [person['address']]

    names.sort()
    sorted_names_with_addresses = []
    for name in names:
        sorted_names_with_addresses.append((name, names_and_addresses[name]))
    return sorted_names_with_addresses

















