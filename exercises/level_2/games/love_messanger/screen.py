import os
import sys
import pyglet
from exercises.level_2.games.love_messanger.message_translator import LoveTranslator


class LoveScreen(pyglet.window.Window):
    def __init__(self, love_msg: LoveTranslator):

        # setting screen size
        pyglet.window.Window.__init__(self, width=1200, height=800, caption="❤MSG")

        # setting screen colors
        r, g, b, alpha = 1.0, 1.0, 1.0, 0.0
        pyglet.gl.glClearColor(r, g, b, alpha)

        self.font = 'Times New Roman'
        self.love_msg = love_msg
        self.label = pyglet.text.Label(
            '🐷 L❤VE  MESSENGER 🐇',
            color=(200, 100, 100, 255),
            font_name=self.font,
            font_size=36,
            x=self.width // 2,
            y=self.height - 36,
            anchor_x='center',
            anchor_y='center')

        animation = pyglet.image.load_animation(f'{__file__.rsplit(os.sep, 1)[0]}{os.sep}o0500026314505904698.gif')
        sprite = pyglet.sprite.Sprite(animation, y=self.height // 2, x=self.width // 2)
        self.bunny = pyglet.sprite.Sprite(
            animation,
            y=self.height - (self.label.font_size*2 + sprite.height),
            x=(self.width // 2) - sprite.width // 2)

        self.text_size = 20
        y = self.height - (self.label.font_size * 2 + sprite.height + self.text_size * 3)

        self.sentence = pyglet.text.Label(
            ' '.join(love_msg.sentence),
            color=(220, 90, 90, 200),
            font_name=self.font,
            font_size=16,
            x=self.width // 2,
            y=y+40,
            anchor_x='center',
            anchor_y='center')


        self.text_x = self.width // 10
        self.text_y = y - self.text_size
        text = []
        language_type_color = (100, 100, 100, 255)
        language_trans_color = (130, 130, 130, 255)
        i = 0
        for language, translation in love_msg.items():
            l1 = pyglet.text.Label(
                language.upper(),
                color=language_type_color,
                font_name=self.font,
                font_size=self.text_size,
                x=self.text_x,
                y=self.text_y)
            try:
                l2 = pyglet.text.Label(
                    translation,
                    color=language_trans_color,
                    font_name=self.font,
                    font_size=self.text_size,
                    x=self.text_x+(self.text_size*20),
                    y=self.text_y)
                text.append(l1)
                text.append(l2)
                self.text_y -= self.text_size * 1.7
                i += 2
                if i == 20:
                    i = 0
                    self.text_y = y - self.text_size
            except TypeError:
                print('failed to render', language, translation)
        self.text = text
        self.i = 0
        self.ticks = 0

    def draw_text(self):
        if len(self.text) > 0:

            for i in range(20):
                if i + self.i >= len(self.text):
                    self.i = 0 - i
                try:
                    self.text[i + self.i].draw()
                except IndexError:
                    self.i = 0 - i
                    self.text[i + self.i].draw()
            self.ticks += 1
            if self.ticks == 20:
                self.i += i
                self.ticks = 0


    def on_draw(self):
        sys.stdout.flush()
        self.clear()
        self.label.draw()
        self.bunny.draw()
        self.sentence.draw()
        self.draw_text()
