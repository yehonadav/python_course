import pyxel


class Hero:
    def __init__(self):
        self.x = 0
        self.y = 52
        self.walk_counter = 0
        self.state = 'idle_right'
        self.models = {
            'idle_right': [
                [0, 0, 0, 16, 16, 0]
            ],
            'idle_left': [
                [0, 0, 0, -16, 16, 0]
            ],
            'walk_right': [
                [0, 0, 0, 16, 16, 0]
            ],
            'walk_left': [
                [0, 0, 0, -16, 16, 0]
            ],
            'walk_down': [
                [0, 0, 0, 16, 16, 0]
            ],
            'walk_up': [
                [0, 0, 0, 16, 16, 0]
            ]
        }

    def draw(self):
        if self.state[:4] == 'walk':
            pyxel.blt(self.x, self.y, *self.models[self.state][self.walk_counter])
        else:
            pyxel.blt(self.x, self.y, *self.models[self.state][self.walk_counter])

class OneBit:
    def __init__(self):
        pyxel.image(0).load(0, 0, 'assets.png')
        self.models = {
            'pine_group_1': [0, 80, 128, 32, 48, 0],
            'pine_group_2': [0, 208, 48, 32, 48, 0],
            'pine_single': [0, 48, 144, 32, 32, 0],
            'pine_single_bare': [0, 112, 144, 32, 32, 0],
            'grass_2': [0, 80, 0, 16, 16, 0],
            'grass_4': [0, 80, 16, 16, 16, 0],
            'tower_cone': [0, 144, 128, 16, 48, 0],
            'tower_broken': [0, 208, 96, 32, 64, 0],
            'rock_wall_1': [0, 16, 96, 16, 16, 0],
            'rock_wall_2': [0, 32, 96, 16, 16, 0]
        }

    def draw(self):
        pyxel.blt(40, 40, *self.models['pine_single'])
        pyxel.blt(70, 0, *self.models['pine_single_bare'])
        pyxel.blt(10, 176, *self.models['pine_single'])
        pyxel.blt(20, 40, *self.models['grass_2'])
        pyxel.blt(60, 38, *self.models['grass_2'])
        pyxel.blt(20, 60, *self.models['grass_4'])
        pyxel.blt(30, 80, *self.models['grass_4'])
