# create classes: Tiger, Wolf, Archer, Player
# player can inherit one of the classes and use them
# Tiger: name, health, method meow(when hurt), method killed
# Wolf: name, health, method bark(when hurt), method killed
# Archer: name, health, method shoot
# player is an archer that kill bad animals
# create a program of a player and some animals, kill them
# add elephant, rhino, give them attack_back method
# use inheritance to improve the code
class Animal:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.is_dead = False

    def killed(self):
        print('{} died from his wounds'.format(self.name))
        self.is_dead = True

class Tiger(Animal):
    def meow(self):
        print('meow... ouch')

    def hurt(self, attacker, amount):
        self.meow()
        self.health -= amount
        if self.health <= 0:
            self.killed()

class Wolf(Animal):
    def bark(self):
        print('bark... ouch')

    def hurt(self, attacker, amount):
        self.bark()
        self.health -= amount
        if self.health <= 0:
            self.killed()


class Elephant(Animal):
    def nose(self):
        print('prrrrr... ouch')

    def hurt(self, attacker, amount):
        self.nose()
        self.health -= amount
        if self.health <= 0:
            self.killed()
        else:
            self.attack_back(attacker)

    def attack_back(self, attaker):
        attaker.hurt(self, 5)


class Rhino(Animal):
    def sound(self):
        print('mmmrr... ouch')

    def hurt(self, attacker, amount):
        self.sound()
        self.health -= amount
        if self.health <= 0:
            self.killed()
        else:
            self.attack_back(attacker)

    def attack_back(self, attaker):
        attaker.hurt(self, 3)


class Archer(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, 100)

    def shoot(self, animal):
        animal.hurt(self, 5)


class Player(Archer):
    def sound(self, amount):
        print('{} is hurt -{}'.format(self.name, amount))

    def hurt(self, attacker, amount):
        self.sound(amount)
        self.health -= amount
        if self.health <= 0:
            self.killed()


class Play:
    def __init__(self):
        print('play archer')
        self.name = input('name your archer:')
        self.player = Player(self.name)

        # create animals
        self.animals = []
        # animals.append(Tiger('tiger', 50))
        # animals.append(Tiger('lion', 90))
        # animals.append(Tiger('leopard', 30))
        self.animals.append(Wolf('wolfi', 10))
        # animals.append(Wolf('fang', 20))
        # animals.append(Wolf('balrog', 15))
        self.animals.append(Wolf('tony', 3))
        self.animals.append(Elephant('elf', 20))
        self.animals.append(Rhino('rino', 15))
        self.main_loop()

    def main_loop(self):
        while True:
            if self.player.is_dead:
                break
            dead = 0
            print('these animals run wild:')
            for animal in self.animals:
                if not animal.is_dead:
                    print(animal.name)
                else:
                    dead += 1
            if len(self.animals) == dead:
                break

            name = input('who do you attack?')
            for animal in self.animals:
                if not animal.is_dead:
                    if animal.name == name:
                        self.player.shoot(animal)
                        break


if __name__ == '__main__':
    Play()
