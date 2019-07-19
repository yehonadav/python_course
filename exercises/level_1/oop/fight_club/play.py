import pygame
from exercises.level_3.snake.game import Game
from exercises.level_3.snake.menu import StartMenu


class Play:
    def __init__(self):
        self.menu = None
        self.game = None
        self.screenX = 1200
        self.screenY = 800
        self.start()

    def run(self, speed, size):
        del self.menu
        self.game = Game(self, speed, size)
        self.game.loop()

    def restart(self):
        del self.game
        self.start()

    def start(self):
        pygame.init()
        self.menu = StartMenu(self)
        self.menu.mainloop()
