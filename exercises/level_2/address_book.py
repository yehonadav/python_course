import os
import pickle

class AddressBook:
    """
    A simple address book application,
    to store, search and delete records
    """
    filename = 'address_book'
    
    def __init__(self, name=None, address=None, email=None, phone=None):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.contacts = {}

    def __str__(self):
        return '[Name: {} | Address: {} | Email: {} | Phone: {}]'.format(self.name, self.address, self.email, self.phone)

    def __repr__(self):
        return '[Name: {} | Address: {} | Email: {} | Phone: {}]'.format(self.name, self.address, self.email, self.phone)

    # Adding details provided by the user in our Address Book
    def add_contacts(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                address_book = open(self.filename, 'rb')
                data = pickle.load(address_book)
                address_book.close()
            else:
                address_book = open(self.filename, 'wb')
                data = {}

            contact = self.get_user_details()
            data[contact['Name']] = contact
            address_book = open(self.filename, 'wb')
            pickle.dump(data, address_book)
            address_book.close()
            print('Contact Added Successfully!')
        except Exception as e:
            print('There was an error:{} Contact was not added.'.format(e))
        finally:
            try:
                address_book.close()
            except: pass
            
    def get_user_details(self):
        try:
            self.contacts['Name'] = str(input('Enter Contact\'s Full Name: '))
            self.contacts['Address'] = str(input('Enter Contact\'s Address: '))
            self.contacts['Email'] = str(input('Enter Contact\'s Email Address: '))
            self.contacts['Phone'] = int(input('Enter Contact\'s Phone Number: '))
            return self.contacts
        except KeyboardInterrupt as error:
            raise error

    def display_contacts(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            address_book = open(self.filename, 'rb')
            data = pickle.load(address_book)
            address_book.close()
            if data:
                for records in data.values():
                    print(records)
            address_book.close()
        else:
            print('No Records in database.')

    def search_contact(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            address_book = open(self.filename, 'rb')
            data = pickle.load(address_book)
            address_book.close()
            try:
                searched_contact = input('Enter the name of the contact to search: ')
                counter = 0
                for contact in data.values():
                    if searched_contact in contact['Name']:
                        print(data[contact['Name']])
                        counter += 1
                if counter == 0:
                    print('No record found whose name is:', searched_contact)
            except Exception as e:
                print('Error occured:{}'.format(e))
        else:
            print('No Records in database.')

    def modify_contact(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            address_book = open(self.filename, 'rb')
            data = pickle.load(address_book)
            address_book.close()
            try:
                contact_modify = input('Enter the full name of the contact to modify: ')
                # Search for the record to update
                for contact in data.values():
                    if contact_modify == contact['Name']:
                        contact = data[contact_modify]
                        break
                option = int(input(
                    'Modify:\n'
                    '(1) name\n'
                    '(2) address\n'
                    '(3) email\n'
                    '(4) phone\n'))
                if option == 1:
                    contact['Name'] = input('Enter New Name: ')
                    del data[contact_modify]
                    data[contact['Name']] = contact
                    print('Successful')
                elif option == 2:
                     contact['Address'] = input('Enter New Address: ')
                     del data[contact_modify]
                     data[contact_modify] = contact
                     print('Successful')
                elif option == 3:
                    contact['Email'] = input('Enter New Email: ')
                    del data[contact_modify]
                    data[contact_modify] = contact
                    print('Successful')
                elif option == 4:
                    contact['Phone'] = input('Enter New Phone: ')
                    del data[contact_modify]
                    data[contact_modify] = contact
                    print('Successful')
                else:
                    print('Incorrect option selected.')
            except:
                print('Error occured. No such record found. Try Again!')
            finally:
                address_book = open(self.filename, 'wb')
                pickle.dump(data, address_book)
                address_book.close()
        else:
            print('No Record in database.')


if __name__ == '__main__':
    myBook = AddressBook()
    while True:
        print(
            '\n\n\n'
            '(1) Add Contacts\n'
            '(2) Search Contact\n'
            '(3) Modify Contact\n'
            '(4) Display All Contacts\n'
            '(5) Exit\n')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            myBook.add_contacts()
        elif choice == 2:
            myBook.search_contact()
        elif choice == 3:
            myBook.modify_contact()
        elif choice == 4:
            myBook.display_contacts()
        elif choice == 5:
            exit()
        else:
            print('Invalid Option. Try Again!')
