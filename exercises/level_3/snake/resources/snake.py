import pygame


def collide(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x3 + x4) > x1 > x3 and (y3 + y4) > y1 > y3 or (x3 + x4) > x2 > x3 and (y3 + y4) > y2 > y3:
        return True
    else:
        return False


def collide2(x1, y1, x2, y2, x3, y3, x4, y4, size):
    if (x3 + (11 * size)) > x1 > x3 - 1 and (y3 + (11 * size)) > y1 > y3 - 1 or (x3 + (11 * size)) > x2 > x3 - 1 and (
            y3 + (11 * size)) > y2 > y3 - 1:
        return True
    else:
        return False


def collide3(x1, y1, x2, y2, x3, y3, x4, y4, size):
    if (x3 + (10 * size)) > x1 > x3 and (y3 + (10 * size)) > y1 > y3 or (x3 + (10 * size)) > x2 > x3 and (
            y3 + (10 * size)) > y2 > y3:
        return True
    else:
        return False


class Snake:
    def __init__(self, speed, size):
        self.position = [20, 20]
        self.image = pygame.Surface((10 * size, 10 * size))
        self.image.fill((0, 255, 0))
        self.speed = speed
        self.size = size
        self.images = []
        self.old_position = [[20, 20]]
        self.direction = [0, 0]
        self.score = 0

    def right(self):
        self.direction = [self.speed, 0]

    def left(self):
        self.direction = [-self.speed, 0]

    def up(self):
        self.direction = [0, -self.speed]

    def down(self):
        self.direction = [0, self.speed]

    def update(self):
        if self.old_position[-1] != self.position:
            self.old_position.append([self.position[0], self.position[1]])
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]
        a = 1
        for x in self.images:
            x[1] = self.old_position[int(a * ((-11 * self.size) / self.speed))]
            a += 1

    def check_collisions(self, x):
        return collide(
            self.position[0],
            self.position[1],
            self.position[0] + 10,
            self.position[1] + 10,
            x[0], x[1], x[0] + 10, x[1] + 10)

    def check_apple(self, x):
        return collide2(
            self.position[0],
            self.position[1],
            self.position[0] + 10,
            self.position[1] + 10,
            x[0], x[1], x[0] + 10, x[1] + 10, self.size)

    def check_collisions2(self, x):
        return collide3(
            self.position[0],
            self.position[1],
            self.position[0] + 10,
            self.position[1] + 10,
            x[0], x[1], x[0] + 10, x[1] + 10, self.size)

    def add_apple(self):
        self.score += 1
        block = pygame.Surface((10 * self.size, 10 * self.size))
        block.fill((0, 255, 0))
        self.images.append([block, [10, 10]])