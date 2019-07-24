import sys
import time
import json
from exercises.level_1.oop.fight_club import conf
from exercises.level_3.snake.game import Game
from exercises.level_1.oop.fight_club.menu import Menu
from exercises.level_1.oop.fight_club.utils.render import render


class Play:
    def __init__(self):
        self.data = {
            "name": None,
            "character": None,
            "exp": 0,
            "health": 100,
            "skills": {},
            "matches": []
        }
        self.file = None
        self.menu = None
        self.game = None
        self.screenX = 1200
        self.screenY = 800
        self.start()

    def save(self):
        with open(self.file, 'w') as f:
            json.dump(self.data, f)

    def load(self, filename: str):
        if not filename.endswith(".json"):
            filename = filename+'.json'

        if filename not in conf.saved_games:
            raise ValueError("game file not found")

        self.file = f'{conf.database_dir}\\{filename}'

        with open(self.file) as f:
            self.data = json.load(f)

    def run(self, speed, size):
        del self.menu
        self.game = Game(self, speed, size)
        self.game.loop()

    def restart(self):
        del self.game
        self.start()

    def start(self):
        self.menu = Menu(self)
        self.menu.start()

    def exit(self, status=None):
        print('FIGHT ☠ CLUB: more blood shall be spilled! bye for now..')
        time.sleep(2)
        render('')
        sys.exit(status=status)
