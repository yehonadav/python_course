from cryptography.fernet import Fernet
from qaviton.utils.random_util import create_random, fake


class SensitiveData:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.storage = Fernet(self.key)

    def encrypt_data(self, data):
        """this will return to the client a decryption key that only he knows about"""
        return self.storage.encrypt(bytes(str(data), encoding='utf-8'))

    def decrypt_data(self, client_key):
        """this will return to the client a decryption of his data using his unique key"""
        return self.storage.decrypt(client_key)


class Client:
    def __init__(self, name, data, storage, third_party):
        self.name = name
        self.key = storage.encrypt_data(data)
        self.storage = storage
        self.third_party = third_party

    def store_data(self, data):
        self.key = self.storage.encrypt_data(data)

    def switch_storage(self, storage):
        data = self.storage.decrypt_data(self.key)
        self.key = storage.encrypt_data(data)
        self.storage = storage

    def send_data_to_third_party(self):
        data = self.storage.decrypt_data(self.key)
        self.third_party.process_data(self, data)


class ThirdParty:
    def process_data(self, client, data):
        for blockchain_transaction in data:
            print(blockchain_transaction)
        self.generate_new_data(client)

    @staticmethod
    def generate_new_data(client):
        new_data = create_random.numbers(length=8)
        client.store_data(new_data)


if __name__ == '__main__':
    storage_unit1 = SensitiveData()
    storage_unit2 = SensitiveData()
    storage_unit3 = SensitiveData()
    storage_unit4 = SensitiveData()

    payment = ThirdParty()

    clients = [
        Client(
            name=fake.name(),
            data=create_random.numbers(length=8),
            storage=storage_unit1,
            third_party=payment
        ) for i in range(10)]

    for client in clients:
        for storage in (storage_unit1, storage_unit2, storage_unit3, storage_unit4):
            client.send_data_to_third_party()
            client.switch_storage(storage)
        client.send_data_to_third_party()
