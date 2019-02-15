# create classes: Tiger, Wolf, Archer, Player
# player can inherit one of the classes and use them
# Tiger: name, health, method meow(when hurt), method killed
# Wolf: name, health, method bark(when hurt), method killed
# Archer: name, health, method shoot
# player is an archer that kill bad Characters
# create a program of a player and some Characters, kill them
# add elephant, rhino, give them attack_back method
# use inheritance to improve the code
class Character:
    def __init__(self, name, health, damage=0, hurt_sound='errrr... '):
        self.name = name
        self.health = health
        self.is_dead = False
        self.damage = damage
        self.hurt_sound = hurt_sound
        
    def killed(self):
        print('{} died from his wounds'.format(self.name))
        self.is_dead = True
    
    def sound(self, play_sound):
        print(play_sound)
        
    def hurt(self, attacker, amount):
        self.sound(self.name + ':' + self.hurt_sound)
        self.sound(self.name + ': took {} damage'.format(amount))
        self.health -= amount
        if self.health <= 0:
            return self.killed()
        self.sound(self.name + ' health: {} '.format(self.health))
        if self.damage > 0:
            self.attack_back(attacker)
    
    def attack_back(self, attaker):
        attaker.hurt(self, self.damage)


class Tiger(Character):
    def __init__(self, name):
        Character.__init__(self, name, 10)


class Wolf(Character):
    def __init__(self, name):
        Character.__init__(self, name, 5)


class Elephant(Character):
    def __init__(self, name):
        Character.__init__(self, name, 20, 5, 'preerr....')


class Rhino(Character):
    def __init__(self, name):
        Character.__init__(self, name, 15, 3)


class Archer(Character):
    def __init__(self, name):
        Character.__init__(self, name, 100, 5)

    def shoot(self, character: Character):
        character.hurt(self, 5)


class Play:
    def __init__(self):
        print('play archer')
        self.name = input('name your archer:')
        self.player = Archer(self.name)

        # create Characters
        self.Characters = []
        # Characters.append(Tiger('tiger', 50))
        # Characters.append(Tiger('lion', 90))
        # Characters.append(Tiger('leopard', 30))
        self.Characters.append(Wolf('wolfi'))
        # Characters.append(Wolf('fang', 20))
        # Characters.append(Wolf('balrog', 15))
        self.Characters.append(Wolf('tony'))
        self.Characters.append(Elephant('elf'))
        self.Characters.append(Rhino('rino'))
        self.main_loop()

    def main_loop(self):
        while True:
            if self.player.is_dead:
                print(self.player.name + ' you lost the game')
                break
            dead = 0
            for character in self.Characters:
                if character.is_dead:
                    dead += 1
            if len(self.Characters) == dead:
                print(self.player + ' you win the game')
                break

            print('\n\nthese Characters run wild:')
            for character in self.Characters:
                if not character.is_dead:
                    print(character.name)

            name = input('\n\nwho do you attack?\n')
            for character in self.Characters:
                if not character.is_dead:
                    if character.name == name:
                        self.player.shoot(character)
                        break


if __name__ == '__main__':
    Play()
