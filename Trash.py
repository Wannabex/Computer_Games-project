import pygame
import Interface
from Interface import ActionWheel
import random


class Trash(pygame.Rect):
    def __init__(self, screen, positionX, positionY, width, height, sprite):
        pygame.Rect.__init__(self, (positionX, positionY, width, height))
        self.name = "Trash"
        self.screen = screen
        self.spriteSheet = sprite
        self.currentImage = self.spriteSheet[0]
        self.imageCount = len(self.spriteSheet)
        self.animationCount = 0
        self.actionsVisible = False
        self.actions = 0

    def update(self):
        self.animation()
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        if self.x <= mouse[Interface.MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[Interface.MOUSE_POS_Y] <= self.y + self.height:
            if mouseClick[Interface.MOUSE_BUTTON_LEFT] and self.actions == 0:
                self.actionsVisible = True


        self.screen.blit(self.currentImage, self)

    def animation(self):
        self.currentImage = self.spriteSheet[self.animationCount // 3]
        self.animationCount += 1
        self.animationCount %= self.imageCount * 3

    def showActionWheel(self, heroWeapon=0, heroConsumable=0):
        self.actions = ActionWheel(self.screen, self.x - ActionWheel.WHEEL_WIDTH - 3, 
                                   self.y - ActionWheel.WHEEL_HEIGHT - 3, weapon=heroWeapon, consumable=heroConsumable)


    def checkHeroWeapon(self, hero):



    def checkHeroConsumable(self, hero):




class Cultist(Trash):
    cultistSprite = [pygame.image.load("./resources/characters/cultist/S1.png"), pygame.image.load("./resources/characters/cultist/S2.png"),
                     pygame.image.load("./resources/characters/cultist/S3.png"), pygame.image.load("./resources/characters/cultist/S4.png")]
    CULTIST_WIDTH = 44
    CULTIST_HEIGHT = 60

    def __init__(self, screen, positionX, positionY):
        Trash.__init__(self, screen, positionX, positionY, self.CULTIST_WIDTH, self.CULTIST_HEIGHT, self.cultistSprite)


class Angel(Trash):
    angelSprite = [pygame.image.load("./resources/characters/angel/S1.png"), pygame.image.load("./resources/characters/angel/S2.png"),
                   pygame.image.load("./resources/characters/angel/S3.png"), pygame.image.load("./resources/characters/angel/S4.png"),
                   pygame.image.load("./resources/characters/angel/S5.png"), pygame.image.load("./resources/characters/angel/S6.png"),
                   pygame.image.load("./resources/characters/angel/S7.png"), pygame.image.load("./resources/characters/angel/S8.png")]
    ANGEL_WIDTH = 122
    ANGEL_HEIGHT = 58

    def __init__(self, screen, positionX, positionY):
        Trash.__init__(self, screen, positionX, positionY, self.ANGEL_WIDTH, self.ANGEL_HEIGHT, self.angelSprite)



class Skeleton(Trash):
    skeletonSprite = [pygame.image.load("./resources/characters/skeleton/S1.png"), pygame.image.load("./resources/characters/skeleton/S2.png"),
                      pygame.image.load("./resources/characters/skeleton/S3.png"), pygame.image.load("./resources/characters/skeleton/S4.png"),
                      pygame.image.load("./resources/characters/skeleton/S5.png"), pygame.image.load("./resources/characters/skeleton/S6.png"),
                      pygame.image.load("./resources/characters/skeleton/S7.png"), pygame.image.load("./resources/characters/skeleton/S8.png"),
                      pygame.image.load("./resources/characters/skeleton/S9.png"), pygame.image.load("./resources/characters/skeleton/S10.png"),
                      pygame.image.load("./resources/characters/skeleton/S11.png")]
    SKELETON_WIDTH = 42
    SKELETON_HEIGHT = 58

    def __init__(self, screen, positionX, positionY):
        Trash.__init__(self, screen, positionX, positionY, self.SKELETON_WIDTH, self.SKELETON_HEIGHT, self.skeletonSprite)