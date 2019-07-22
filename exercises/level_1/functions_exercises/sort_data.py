import random


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


def add_random_postal(names_with_addresses):
    names_with_addresses_and_postal = []
    for i in names_with_addresses:
        names_with_addresses_and_postal.append((
            i[0],
            i[1],
            str(random.randint(0, 10)) +
            str(random.randint(0, 10)) +
            str(random.randint(0, 10)) +
            str(random.randint(0, 10)) +
            str(random.randint(0, 10))
        ))
    return names_with_addresses_and_postal


def sum_postal_codes(data):
    postal = 0
    for i in data:
        postal += int(i[2])
    return postal
