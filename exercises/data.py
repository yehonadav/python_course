import random
from faker import Faker
fake = Faker()


def get_data(size=10):
    data = []
    for _ in range(size):
        data.append({
            'name': fake.name(),
            'address': fake.address(),
            'age': random.randint(0, 121),
            'birth': random.randint(1900, 2019),
            'automotive_number': fake.license_plate(),
            'bank_acount': fake.iban(),
            'favorite_color': fake.safe_color_name(),
            'company': fake.company(),
            'catch_phrase': fake.catch_phrase(),
            'email': fake.email()
        })
    return data
