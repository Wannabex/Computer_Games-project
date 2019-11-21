import pygame
import Interface
import Building
import random


class Trash(pygame.Rect):
    def __init__(self, screen, building, width, height, sprite):
        self.screen = screen
        self.building = building
        pygame.Rect.__init__(self, (0, 0, width, height))
        self.name = "Trash"
        self.description = "Enemy"
        self.spriteSheet = sprite
        self.currentImage = self.spriteSheet[0]
        self.imageCount = len(self.spriteSheet)
        self.animationCount = 0
        self.fpsRatio = 3
        self.clickable = True
        self.actionsVisible = False
        self.physicalPower = 0
        self.mentalPower = 0
        self.dead = False

    def spawn(self):
        self.building.spawnObject(self)

    def update(self):
        if not self.dead:
            self.animation()
            mouse = pygame.mouse.get_pos()
            mouseClick = pygame.mouse.get_pressed()
            if self.x <= mouse[Interface.MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[Interface.MOUSE_POS_Y] <= self.y + self.height:
                if mouseClick[Interface.MOUSE_BUTTON_LEFT] and self.clickable:
                    self.actionsVisible = True
            self.screen.blit(self.currentImage, self)
        else:
            del self

    def animation(self):
        self.currentImage = self.spriteSheet[self.animationCount // self.fpsRatio]
        self.animationCount += 1
        self.animationCount %= self.imageCount * self.fpsRatio

    def wheelEvents(self, clicked):
        if clicked == 0:
            self.actionsVisible = False
        if clicked == 1:
            self.actionsVisible = False
        if clicked == 2:
            self.actionsVisible = False
            return 1
        if clicked == 3:
            self.actionsVisible = False
        if clicked == 4:
            self.actionsVisible = False



class Cultist(Trash):
    cultistSprite = [pygame.image.load("./resources/characters/cultist/S1.png"), pygame.image.load("./resources/characters/cultist/S2.png"),
                     pygame.image.load("./resources/characters/cultist/S3.png"), pygame.image.load("./resources/characters/cultist/S4.png")]
    CULTIST_WIDTH = 44
    CULTIST_HEIGHT = 60

    def __init__(self, screen, building):
        Trash.__init__(self, screen, building, self.CULTIST_WIDTH, self.CULTIST_HEIGHT, self.cultistSprite)
        self.name = "Cultist"
        self.description = "This is Cultist"
        self.fpsRatio = 9
        self.physicalPower = 10
        self.mentalPower = 15

class Angel(Trash):
    angelSprite = [pygame.image.load("./resources/characters/angel/S1.png"), pygame.image.load("./resources/characters/angel/S2.png"),
                   pygame.image.load("./resources/characters/angel/S3.png"), pygame.image.load("./resources/characters/angel/S4.png"),
                   pygame.image.load("./resources/characters/angel/S5.png"), pygame.image.load("./resources/characters/angel/S6.png"),
                   pygame.image.load("./resources/characters/angel/S7.png"), pygame.image.load("./resources/characters/angel/S8.png")]
    ANGEL_WIDTH = 122
    ANGEL_HEIGHT = 117

    def __init__(self, screen, building):
        Trash.__init__(self, screen, building, self.ANGEL_WIDTH, self.ANGEL_HEIGHT, self.angelSprite)
        self.name = "Seraph"
        self.description = "This is Seraph"
        self.y = random.choice(self.building.floorsYs[:1]) - self.ANGEL_HEIGHT
        self.physicalPower = 20
        self.mentalPower = 35



class Skeleton(Trash):
    skeletonSprite = [pygame.image.load("./resources/characters/skeleton/S1.png"), pygame.image.load("./resources/characters/skeleton/S2.png"),
                      pygame.image.load("./resources/characters/skeleton/S3.png"), pygame.image.load("./resources/characters/skeleton/S4.png"),
                      pygame.image.load("./resources/characters/skeleton/S5.png"), pygame.image.load("./resources/characters/skeleton/S6.png"),
                      pygame.image.load("./resources/characters/skeleton/S7.png"), pygame.image.load("./resources/characters/skeleton/S8.png"),
                      pygame.image.load("./resources/characters/skeleton/S9.png"), pygame.image.load("./resources/characters/skeleton/S10.png"),
                      pygame.image.load("./resources/characters/skeleton/S11.png")]
    SKELETON_WIDTH = 42
    SKELETON_HEIGHT = 58

    def __init__(self, screen, building):
        Trash.__init__(self, screen, building, self.SKELETON_WIDTH, self.SKELETON_HEIGHT, self.skeletonSprite)
        self.name = "Skeleton"
        self.description = "This is skeleton"
        self.physicalPower = 40
        self.mentalPower = 5

