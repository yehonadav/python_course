# create classes: Tiger, Wolf, Archer, Player
# player can inherit one of the classes and use them
# Tiger: name, health, method meow(when hurt), method killed
# Wolf: name, health, method bark(when hurt), method killed
# Archer: name, health, method shoot
# player is an archer that kill bad animals
# create a program of a player and some animals, kill them
# add elephant, rhino, they add attack back
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

    def hurt(self, amount):
        self.meow()
        self.health -= amount
        if self.health <= 0:
            self.killed()

class Wolf(Animal):
    def bark(self):
        print('bark... ouch')

    def hurt(self, amount):
        self.bark()
        self.health -= amount
        if self.health <= 0:
            self.killed()

class Archer(Animal):
    def __init__(self, name):
        Animal.__init__(self, name, 100)

    def shoot(self, animal):
        animal.hurt(5)

class Player(Archer):
    pass


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
        self.main_loop()

    def main_loop(self):
        while True:
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
