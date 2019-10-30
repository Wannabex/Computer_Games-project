import pygame
import random

WHITE = (0, 0, 0)
COLOURS = (9, 23, 128), (11, 34, 181), (6, 30, 189), (3, 26, 173), (25, 41, 145), (33, 46, 133), (18, 30, 110)
DROPSIZE = 10

row_height =  0.6 * DROPSIZE
row_width = DROPSIZE

class Column():
    def __init__(self, x, screen, screenInfo):

        self.x = x
        self.screen = screen
        self.windowX = screenInfo.current_w - 400
        self.windowY =  screenInfo.current_h - 200
        self.clear_and_restart(1000)

    def clear_and_restart(self, start_pos = 250):
        pygame.draw.rect(self.screen, WHITE, (self.x  - row_width//2, 0, row_width, Y))
        self.list = []
        self.y = random.randint(0, start_pos // row_height) * row_height
        self.fadeAge = random.randint(20, 40)
        self.fadeSpeed = random.randint(9, 15)

    def add_droplet(self):
        if 0 < self.y < self.windowY:
            self.list.append()

    def move(self):
        self.y += row_height
        self.add_droplet()

    def update(self):
        for


class Droplet():
    def __init__(self, column):
        self.x = column.x
        self.y = column.y
        self.colour = random.choice(COLOURS)
        self.age = 0
        self.fadeAge = column.fadeAge + random.randint(-10, 10)
        self.fadeSpeed = column.fadeSpeed + random.randint(-5, 5)

    def update(self):
        self.draw()
        self.age += 1

    def draw(self):
        self.surf = font.render