import pygame
import random

ENEMY_WIDTH = 60
ENEMY_HEIGHT = 60

class Trash(object):
    cultist = [pygame.image.load("./resources/characters/cultist/S1.png"), pygame.image.load("./resources/characters/cultist/S2.png"), pygame.image.load("./resources/characters/cultist/S3.png"),
               pygame.image.load("./resources/characters/cultist/S4.png"), pygame.image.load("./resources/characters/cultist/S5.png"), pygame.image.load("./resources/characters/cultist/S6.png"),
               pygame.image.load("./resources/characters/cultist/S7.png"), pygame.image.load("./resources/characters/cultist/S8.png"), pygame.image.load("./resources/characters/cultist/S9.png"),
               pygame.image.load("./resources/characters/cultist/S10.png"), pygame.image.load("./resources/characters/cultist/S11.png"), pygame.image.load("./resources/characters/cultist/S12.png")]


    def __init__(self, screen, positionX, positionY):
        pygame.Rect.__init__(self, (positionX, positionY, ENEMY_WIDTH, ENEMY_HEIGHT))
        self.name = "Trasher"
        self.enemyImage = self.cultist


    def update(self):
        self.animation()
        self.screen.blit(self.playerImage, self)


    def animation(self):
        self.playerImage = self.walkLeft[self.walkCount//3]
            self.walkCount += 1
        elif self.goingRight:
            self.playerImage = self.walkRight[self.walkCount // 3]
            self.walkCount += 1
        else:
            self.playerImage = self.stay
        self.walkCount %= 27

