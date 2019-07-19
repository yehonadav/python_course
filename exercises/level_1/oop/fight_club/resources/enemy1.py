# player = """
#
#
#
#                 \ \ /\ / /
#               \            /
#               \            /
#                 \\\_  _///
#                 _|  \/  |_
#              __/   \  /   \__
#         //--|       ||       |--\\_
#       /   --      _/  \_           \
#       | /  _   \_        _/   _  \  |
#       /    |     \      /     |   \/\
#      /     |\    |  ||  |    /|    \||
#     | /|   ||\    \ || /    / |  |\ ||
#     || |  //  |    \  /    |  \  | ||/
#               --------------
# """
import random
from exercises.level_1.oop.fight_club.resources.animations import enemy1 as animation
from exercises.level_1.oop.fight_club.resources.base_class import hurting, attacking, Character, attack_types, attack_meta


class Enemy1(Character):
    def __init__(self, name):
        attacks = {
            "lightning strike": self.lightning_strike
        }
        Character.__init__(
            self,
            name,
            health=20,
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
            lines = lines + [self.length * ' '] * (self.height - len(lines)) if self.height - len(lines) > 0 else lines
            frames[i] = '\n'.join(lines)
        return frames

    def hurt(self, attack_meta):
        self.health -= attack_meta.dmg
        if self.is_dead():
            animation = self.dead_animation
            msg = f'{self.name} took {attack_meta.dmg} points of damage and died!'
        else:
            animation = self.hurt_animation
            msg = f'{self.name} took {attack_meta.dmg} points of damage'
        return hurting(animation, attack_meta, msg)

    def lightning_strike(self, enemy: Character):
        dmg = random.randint(1, 4)
        critical_x2 = random.randint(0, 3)
        if critical_x2 == 3:
            dmg *= 2
            critical_x2 = random.randint(0, 3)
            if critical_x2 == 3:
                dmg *= 2
                msg = f'{self.name} attacks with a critical x4 hit of {dmg} points of damage!'
            else:
                msg = f'{self.name} attacks with a critical x2 hit of {dmg} points of damage!'
        else:
            msg = f'{self.name} attacks with {dmg} points of damage'

        types = [attack_types.electricity]
        meta = attack_meta(dmg, types, self.enhancements, self.curses)
        return attacking(self.attack_animation, msg, enemy.hurt(meta))
