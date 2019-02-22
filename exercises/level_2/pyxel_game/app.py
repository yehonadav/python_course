import pyxel
from exercises.level_2.pyxel_game.models import Hero, OneBit


class App:
    def __init__(self):
        pyxel.init(255, 255, caption='pyxel game')
        self.OneBit = OneBit()
        self.hero = Hero()
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()

    def update_player(self):
        if self.hero.state[5:] == 'right' or self.hero.state[5:] == 'left':
            self.hero.state = 'idle' + '_' + self.hero.state[5:]

        if pyxel.btn(pyxel.KEY_D):
            # player is moving right
            self.hero.state = 'walk_right'
            self.hero.x = min(self.hero.x + 2, pyxel.width - 20)
            return

        if pyxel.btn(pyxel.KEY_A):
            # player is moving left
            self.hero.state = 'walk_left'
            self.hero.x = max(self.hero.x - 2, 0)
            return

        if pyxel.btn(pyxel.KEY_W):
            self.hero.state = 'walk_up'
            self.hero.y = max(self.hero.y - 2, -10)
            return

        if pyxel.btn(pyxel.KEY_S):
            self.hero.state = 'walk_down'
            self.hero.y = min(self.hero.y + 2, pyxel.height - 20)
            return

    def draw(self):
        pyxel.cls(7)
        pyxel.pal(1, 0)
        pyxel.text(200, 230, 'x: {}\ny: {}'.format(self.hero.x, self.hero.y), 1)
        self.OneBit.draw()
        self.hero.draw()
