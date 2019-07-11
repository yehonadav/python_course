import random
from faker import Faker
fake = Faker()


def create_user():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'age': random.randint(0, 121),
        'birth': random.randint(1900, 2019),
        'automotive_number': fake.license_plate(),
        'bank_account': fake.iban(),
        'favorite_color': fake.safe_color_name(),
        'company': fake.company(),
        'catch_phrase': fake.catch_phrase(),
        'email': fake.email()
    }


def get_data(size=10):
    return [create_user() for _ in range(size)]


def get_data_as_text(size=10):
    return ''.join([
        ''.join([
            f'{key}: {value}\n'
            for key, value in create_user().items()
        ])
        for _ in range(size)
    ])


def transform_data_to_text(data: list):
    return ''.join([
        ''.join([
            f'{key}: {value}\n'
            for key, value in item.items()
        ])
        for item in data
    ])
