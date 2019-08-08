class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        self.address = None

    def add_address(self, address):
        self.address = address

    def info(self, address=None):
        if not address:
            if not self.address:
                raise Exception(self.name + ' has missing address, please enter or update the address')
            address = self.address
        print(self.name + ' is ' + str(self.age) + ' years old and lives in ' + address)

p1 = Person('jon', 16)
p2 = Person('dor', 23)
p3 = Person('ran', 18)

p1.add_address('israel ashdod hameyasdim 53')
p1.info()
p2.info()
p3.info('israel ashdod hameyasdim 51')
print(p1.address)
print(p2.address)


from exercises.data import get_data

people = get_data(10)

dudes = []
for dude in people:
    dudes.append(Person(dude['name'], dude['age']))


for dude in dudes:
    dude.info()
