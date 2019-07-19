import sys
import pygame


class StartMenu:
    def __init__(self, game):
        self.game = game
        self.screen = pygame.display.set_mode((self.game.screenX, self.game.screenY))
        self.b1 = '({}, 300,100,50),"Start", [(0,255,0), (0,150,0)], action = self.choose_size'.format(int(self.game.screenX*(20/100))-50)
        self.b2 = '({}, 300,100,50),"Exit", [(255,0,0), (150,0,0)], action = self.exit'.format(int(self.game.screenX*(80/100))-50)
        self.buttons = [self.b1, self.b2]
        self.blocks = []
        self.size = 1
        self.click0 = self.loads = False
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

    def make_text(self, x, y, text, size=20, color=(0, 0, 0), a=False):
        txts = pygame.font.SysFont('Courier New', size).render(text, True, color)
        txtrect = txts.get_rect()
        txtrect.topleft = (x, y)
        if a:
            txtrect.center = (x, y)
        self.screen.blit(txts, txtrect)

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
        self.make_text((position[0] + position[2] / 2), (position[1] + position[3] / 2), text, a=True, size=textsize)

    def mainloop(self):
        while 1:
            self.screen.fill((30, 40, 100))
            self.make_text(self.game.screenY, 150, 'Fight Club', color=(255, 255, 255), size=100, a=True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            for x in self.blocks:
                self.screen.blit(x[0], x[1])
            for x in self.buttons:
                exec('self.make_button(' + x + ')')
                if self.hover:
                    click = pygame.mouse.get_pressed()
                    if click[0] == 1:
                        self.click0 = True
                    if self.click0:
                        if click[0] == 0:
                            self.buttonclick()
                            self.click0 = False
            pygame.display.update()

    def choose_chracter(self):
        self.b1 = '({}, 300,100,50),"Small", [(0,255,0), (0,150,0)], action = self.small'.format(int(self.game.screenX * (20/100)) - 50)
        self.b2 = '({}, 300,100,50),"Normal", [(0,255,0), (0,150,0)], action = self.choose_difficulty'.format(int(self.game.screenX * (50/100)) - 50)
        self.b3 = '({}, 300,100,50),"Big", [(0,255,0), (0,150,0)], action = self.big'.format(int(self.game.screenX * (80 / 100)) - 50)
        self.buttons = [self.b1, self.b2, self.b3]

    def small(self):
        self.size = 0.5
        self.choose_difficulty()

    def big(self):
        self.size = 2
        self.choose_difficulty()

    def choose_difficulty(self):
        self.b1 = '({}, 300,100,50),"Easy", [(0,255,0), (0,150,0)], action = self.easy'.format(int(self.game.screenX * (20/100)) - 50)
        self.b2 = '({}, 300,100,50),"Normal", [(0,255,0), (0,150,0)], self.normal'.format(int(self.game.screenX * (40/100)) - 50)
        self.b3 = '({}, 300,100,50),"Hard", [(0,255,0), (0,150,0)], action = self.hard'.format(int(self.game.screenX * (60/100)) - 50)
        self.b4 = '({}, 300,100,50),"Expert", [(0,255,0), (0,150,0)], action = self.expert'.format(int(self.game.screenX * (80/100)) - 50)
        self.buttons = [self.b1, self.b2, self.b3, self.b4]

    def easy(self):
        self.game.run(0.25, self.size)

    def normal(self):
        self.game.run(0.5, self.size)

    def hard(self):
        self.game.run(1, self.size)

    def expert(self):
        self.game.run(2, self.size)

    def exit(self):
        sys.exit()
