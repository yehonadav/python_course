import abc


class attack_types:
    physical = 0
    magical = 1
    ranged = 2
    chemical = 3
    biological = 4
    fire = 5
    ice = 6
    light = 7
    electricity = 8


class attack_meta:
    def __init__(self, dmg, types, enhancements=None, curses=None):
        self.dmg = dmg
        self.types = types
        self.curses = curses
        self.enhancements = enhancements


class hurting:
    def __init__(self, animation, attacker: attack_meta, hurt_msg):
        self.animation = animation
        self.attacker = attacker
        self.hurt_msg = hurt_msg


class attacking:
    def __init__(self, animation, attack_msg, hurted: hurting):
        self.animation = animation
        self.attack_msg = attack_msg
        self.hurted = hurted


class Character(metaclass=abc.ABCMeta):
    def __init__(
            self,
            name: str,
            health: int,
            attacks: dict,
            height: int,
            length: int,
            idle_animation: list,
            attack_animation: list,
            hurt_animation: list,
            dead_animation: list):
        self.height = height
        self.length = length
        self.idle_animation = self.normalize_frames(idle_animation)
        self.attack_animation = self.normalize_frames(attack_animation)
        self.hurt_animation = self.normalize_frames(hurt_animation)
        self.dead_animation = self.normalize_frames(dead_animation)

        self.name = name
        self.health = health
        self.attacks = attacks
        self.curses = None
        self.enhancements = None

    @abc.abstractmethod
    def normalize_frames(self, frames):
        raise NotImplementedError

    def is_alive(self):
        return self.health > 0

    def is_dead(self):
        return self.health <= 0

    def hurt(self, attack_meta):
        self.health -= attack_meta.dmg
        if self.is_dead():
            animation = self.dead_animation
            msg = f'{self.name} took {attack_meta.dmg} points of damage and died!'
        else:
            animation = self.hurt_animation
            msg = f'{self.name} took {attack_meta.dmg} points of damage'
        return hurting(animation, attack_meta, msg)
