import pygame
import random

COLORS = [(9, 23, 128), (11, 34, 181), (6, 30, 189), (3, 26, 173), (25, 41, 145), (33, 46, 133), (18, 30, 110)]
SIZE = 6

class Column(object):
    def __init__(self, x, screen, maxAge):
        self.x = x
        self.maxAge = maxAge
        self.spawnCounter = 0
        self.spawnRate = random.randint(2, 20)
        self.screen = screen
        self.list = []

    def update(self):
        self.spawnCounter += 1
        if self.spawnCounter == self.spawnRate:
            self.list.append(Droplet(self, self.maxAge))
            self.spawnRate = random.randint(2, 20)
            self.spawnCounter = 0
        for droplet in self.list:
            droplet.update()


class Droplet(object):
    def __init__(self, column, maxAge):
        self.screen = column.screen
        self.x = column.x
        self.y = 0
        self.size = random.randint(1, 4)
        self.color = random.choice(COLORS)
        self.age = random.randint(30, maxAge)
        self.speed = random.randint(10, 18)
        self.font = pygame.font.Font(None, SIZE)

    def update(self):
        self.y += self.speed
        if not self.y >= self.age:
            pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y + self.size), self.size // 2)
        else:
            del self


class Sky(object):
    thunders = [pygame.image.load("./resources/images/environment/thunder1.png"), pygame.image.load("./resources/images/environment/thunder2.png"), pygame.image.load("./resources/images/environment/thunder3.png"),
              pygame.image.load("./resources/images/environment/thunder4.png")]
    monsters = [pygame.image.load("./resources/images/environment/monster1.png"), pygame.image.load("./resources/images/environment/monster2.png"), pygame.image.load("./resources/images/environment/monster3.png")]

    def __init__(self, screen, screenWidth, screenHeight, leftWallX, rightWallX, ceilingY):
        self.screen = screen
        self.thunder = SomethingInTheSky(screen, self.thunders, screenWidth - 50, screenHeight - 100, leftWallX - 25, rightWallX, ceilingY)
        self.monster = SomethingInTheSky(screen, self.monsters, screenWidth - 100, screenHeight - 100, leftWallX - 100, rightWallX - 100, ceilingY)

    def update(self):
        self.monster.appear()
        self.thunder.appear()



class SomethingInTheSky(pygame.Rect):
    def __init__(self, screen, images, screenWidth, screenHeight, leftWallX, rightWallX, ceilingY):
        pygame.Rect.__init__(self, (0, 0, 1, 1))
        self.images = images
        self.screen = screen
        self.skyWidth = screenWidth
        self.skyHeight = screenHeight // 2
        self.leftWallX = leftWallX
        self.rightWallX = rightWallX
        self.ceilingY = ceilingY
        self.shownTime = 0
        self.appearanceTime = 0
        self.itsTime = False

    def appear(self):
        if self.itsTime:
            if self.appearanceTime == 0:
                screenSide = random.randint(1, 3)
                if screenSide == 1:
                    self.x = random.randint(-50, self.leftWallX)
                    self.y = random.randint(-50, self.skyHeight)
                elif screenSide == 2:
                    self.x = random.randint(-50, self.skyWidth + 50)
                    self.y = random.randint(-50, self.ceilingY - 50)
                else:
                    self.x = random.randint(self.rightWallX, self.skyWidth - 50)
                    self.y = random.randint(-50, self.skyHeight)
                self.appearanceTime = random.randint(1, 3)
                self.thunderImage = random.choice(self.images)
            if self.shownTime < self.appearanceTime:
                self.update()
                self.shownTime += 1
            if self.shownTime >= self.appearanceTime:
                self.appearanceTime = 0
                self.shownTime = 0
                self.itsTime = False

    def update(self):
        self.screen.blit(self.thunderImage, self)

