import pygame
import random

ENEMY_WIDTH = 60
ENEMY_HEIGHT = 60

class Trash(pygame.Rect):
    cultist = [pygame.image.load("./resources/characters/cultist/S1.png"), pygame.image.load("./resources/characters/cultist/S2.png"), pygame.image.load("./resources/characters/cultist/S3.png"),
               pygame.image.load("./resources/characters/cultist/S4.png"), pygame.image.load("./resources/characters/cultist/S5.png"), pygame.image.load("./resources/characters/cultist/S6.png"),
               pygame.image.load("./resources/characters/cultist/S7.png"), pygame.image.load("./resources/characters/cultist/S8.png"), pygame.image.load("./resources/characters/cultist/S9.png"),
               pygame.image.load("./resources/characters/cultist/S10.png"), pygame.image.load("./resources/characters/cultist/S11.png"), pygame.image.load("./resources/characters/cultist/S12.png")]


    def __init__(self, screen, positionX, positionY):
        pygame.Rect.__init__(self, (positionX, positionY, ENEMY_WIDTH, ENEMY_HEIGHT))
        self.name = "Trasher"
        self.screen = screen
        self.characterImage = self.cultist
        self.animationCount = 0

    def update(self):
        self.animation()
        self.screen.blit(self.characterImage, self)

    def animation(self):
        self.characterImage = self.cultist[self.animationCount // 3]
        self.animationCount += 1
        self.animationCount %= 27

