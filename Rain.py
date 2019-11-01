import pygame
import random

COLORS = [(9, 23, 128), (11, 34, 181), (6, 30, 189), (3, 26, 173), (25, 41, 145), (33, 46, 133), (18, 30, 110)]
SIZE = 6

class Column():
    def __init__(self, x, screen):
        self.x = x
        self.spawnCounter = 0
        self.spawnRate = random.randint(10, 70)
        self.screen = screen
        self.list = []

    def update(self):
        self.spawnCounter += 1
        if self.spawnCounter == self.spawnRate:
            self.list.append(Droplet(self))
            self.spawnRate = random.randint(10, 70)
            self.spawnCounter = 0
        for droplet in self.list:
            droplet.update()


class Droplet():
    def __init__(self, column):
        self.screen = column.screen
        self.x = column.x
        self.y = 0
        self.size = random.randint(1, 4)
        self.color = random.choice(COLORS)
        self.age = random.randint(200, 1000)
        self.speed = random.randint(9, 16)
        self.font = pygame.font.Font(None, SIZE)

    def update(self):
        self.y += self.speed
        if not self.y >= self.age:
            pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y + self.size), self.size // 2)
        else:
            del self


