import random
from exercises.level_1.oop.fight_club.resources.animations import player1 as animation
from exercises.level_1.oop.fight_club.resources.base_class import hurting, attacking, Character, attack_meta, attack_types


class Homer(Character):
    def __init__(self, name):
        attacks = {
            "fart": self.attack_fart
        }
        Character.__init__(
            self,
            name,
            health=100,
            height=50,
            length=60,
            attacks=attacks,
            idle_animation=animation.idle,
            attack_animation=animation.attack,
            hurt_animation=animation.hurt,
            dead_animation=animation.dead
        )

    def normalize_frames(self, frames):
        for i, frame in enumerate(frames):
            lines = [line + (self.length - len(line)) * ' ' for line in frame.split('\n')]
            lines = [self.length * ' '] * (self.height - len(lines)) + lines if self.height - len(lines) > 0 else lines
            frames[i] = '\n'.join(lines)
        return frames

    def hurt(self, attack_meta: attack_meta):
        self.health -= attack_meta.dmg
        if self.is_dead():
            animation = self.dead_animation
            msg = f'{self.name} took {attack_meta.dmg} points of damage and died!'
        else:
            animation = self.hurt_animation
            msg = f'{self.name} took {attack_meta.dmg} points of damage'
        return hurting(animation, attack_meta, msg)

    def attack_fart(self, enemy: Character):
        dmg = random.randint(5, 7)
        types = [attack_types.chemical]
        meta = attack_meta(dmg, types, self.enhancements, self.curses)
        critical = random.randint(0, 3)
        if critical == 3:
            dmg *= 2
            msg = f'{self.name} attacks with a critical hit of {dmg} points of damage!'
        else:
            msg = f'{self.name} attacks with {dmg} points of damage'
        return attacking(self.attack_animation, msg, enemy.hurt(meta))
