import sys
import pygame
from exercises.level_3.snake.resources.snake import Snake
from exercises.level_3.snake.resources.apple import Apple


class Game:
    def __init__(self, game, speed, size=1):
        self.game = game
        self.screen = pygame.display.set_mode((self.game.screenX, self.game.screenY))
        pygame.display.set_caption('Snake Game')
        self.snake = Snake(speed, size)
        self.blocks = []
        self.score = 0
        self.size = size
        self.left = self.right = self.up = self.down = False
        self.hover = False
        self.click0 = False
        color = (0, 0, 0)
        for x in range(0, self.game.screenX, 10):
            t = pygame.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 0]])
        for x in range(0, self.game.screenX, 10):
            t = pygame.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, self.game.screenY-10]])
        for x in range(0, self.game.screenY, 10):
            t = pygame.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [0, x]])
        for x in range(0, self.game.screenY, 10):
            t = pygame.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [self.game.screenX-10, x]])
        self.apple = Apple(size)

    def over(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for x in self.blocks:
                self.screen.blit(x[0], x[1])

            text = pygame.font.SysFont('Courier New', 55).render('Game Over', True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topleft = (int(self.game.screenX * (50/100)) - 150, 80)
            self.screen.blit(text, text_rect)

            text = pygame.font.SysFont('Courier New', 45).render('Score: {}'.format(str(self.snake.score)), True, (255, 255, 255))
            text_rect = text.get_rect()
            text_rect.topleft = (int(self.game.screenX * (50 / 100)) - 120, 160)
            self.screen.blit(text, text_rect)

            pygame.display.update()
            self.make_button((int(self.game.screenX * (50 / 100)) - 50, 300, 100, 50), 'Restart', [(255, 255, 255), (150, 150, 150)],
                             action=lambda: self.game.restart())
            if self.hover:
                click = pygame.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True
                if self.click0:
                    if click[0] == 0:
                        self.buttonclick()
                        self.click0 = False

    def make_button(self, position, text, color, action=None, textsize=20):
        mouse = pygame.mouse.get_pos()
        old_position = position
        rect = pygame.Rect(position)
        rect.topleft = 0, 0
        rectangle = pygame.Surface(rect.size, pygame.SRCALPHA)

        circle = pygame.Surface([min(rect.size) * 3] * 2, pygame.SRCALPHA)
        pygame.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle = pygame.transform.smoothscale(circle, [int(min(rect.size) * 0.5)] * 2)

        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        position = old_position
        if (position[0] + position[2]) > mouse[0] > position[0] and (position[1] + position[3]) > mouse[1] > position[1]:
            self.hover = True
            self.buttonclick = action
            color = pygame.Color(*color[1])
            alpha = color.a
            color.a = 0
        else:
            color = pygame.Color(*color[0])
            alpha = color.a
            color.a = 0
            self.hover = False
        rectangle.fill(color, special_flags=pygame.BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MIN)
        self.screen.blit(rectangle, position)
        txts = pygame.font.SysFont('Courier New', textsize).render(text, True, (0, 0, 0))
        txtrect = txts.get_rect()
        txtrect.center = (position[0] + position[2] / 2), (position[1] + position[3] / 2)
        self.screen.blit(txts, txtrect)

    def reset(self):
        self.left, self.right, self.up, self.down = False, False, False, False

    def loop(self):
        self.game_over = False
        while not self.game_over:
            self.screen.fill((30, 40, 100))
            self.snake.update()
            for x in self.blocks:
                if self.snake.check_collisions(x[1]):
                    self.over()
                self.screen.blit(x[0], x[1])
            a = 0
            for x in self.snake.images:
                if a != 0:
                    if self.snake.check_apple(x[1]):
                        self.over()
                self.screen.blit(x[0], x[1])
                a += 1
            if self.snake.check_apple(self.apple.position):
                self.snake.add_apple()
                del self.apple
                self.apple = Apple(self.size)
            self.screen.blit(self.apple.image, self.apple.position)
            self.screen.blit(self.snake.image, self.snake.position)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if not self.left:
                            self.reset()
                            self.snake.right()
                            self.right = True
                    elif event.key == pygame.K_LEFT:
                        if not self.right:
                            self.reset()
                            self.snake.left()
                            self.left = True
                    elif event.key == pygame.K_UP:
                        if not self.down:
                            self.reset()
                            self.snake.up()
                            self.up = True
                    elif event.key == pygame.K_DOWN:
                        if not self.up:
                            self.reset()
                            self.snake.down()
                            self.down = True
            pygame.display.update()
