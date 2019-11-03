import pygame
import random


MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

CHARACTER_HEIGHT = 64
CHARACTER_WIDTH = 64


class Player(pygame.Rect):
    walkLeft = [pygame.image.load("./resources/characters/hero/L1.png"), pygame.image.load("./resources/characters/hero/L2.png"), pygame.image.load("./resources/characters/hero/L3.png"),
                pygame.image.load("./resources/characters/hero/L4.png"), pygame.image.load("./resources/characters/hero/L5.png"), pygame.image.load("./resources/characters/hero/L6.png"),
                pygame.image.load("./resources/characters/hero/L7.png"), pygame.image.load("./resources/characters/hero/L8.png"), pygame.image.load("./resources/characters/hero/L9.png")]

    walkRight = [pygame.image.load("./resources/characters/hero/R1.png"), pygame.image.load("./resources/characters/hero/R2.png"), pygame.image.load("./resources/characters/hero/R3.png"),
                 pygame.image.load("./resources/characters/hero/R4.png"), pygame.image.load("./resources/characters/hero/R5.png"), pygame.image.load("./resources/characters/hero/R6.png"),
                 pygame.image.load("./resources/characters/hero/R7.png"), pygame.image.load("./resources/characters/hero/R8.png"), pygame.image.load("./resources/characters/hero/R9.png")]
    stay = pygame.image.load("./resources/characters/hero/standing.png")

    def __init__(self, screen, positionX, positionY):
        pygame.Rect.__init__(self, (positionX, positionY, CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.screen = screen
        self.playerImage = self.stay
        self.speed = 5
        self.goingLeft = False
        self.goingRight = False
        self.moving = False
        self.walkCount = 0
        self.health = random.randint(30, 70)
        self.mentality = 30 + 70 - self.health
        self.weapon = "Hands"
        self.consumable = "Bread"
        self.experience = 0
        self.statusChanged = False

    def update(self):
        self.animation()
        if self.moving:
            self.moveToDestination()
        self.screen.blit(self.playerImage, self)


    def animation(self):
        if self.goingLeft:
            self.playerImage = self.walkLeft[self.walkCount//3]
            self.walkCount += 1
        elif self.goingRight:
            self.playerImage = self.walkRight[self.walkCount // 3]
            self.walkCount += 1
        else:
            self.playerImage = self.stay
        self.walkCount %= 27

    def control(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        if mouseClick[MOUSE_BUTTON_LEFT] and self.leftWallX <= mouse[MOUSE_POS_X] <= self.rightWallX + self.width // 2:
            destination = mouse[MOUSE_POS_X] - self.width // 2
            if self.leftWallX - self.width // 2 <= destination <= self.leftWallX:
                destination = destination + self.width // 2
            elif self.rightWallX - self.width // 2 <= destination <= self.rightWallX:
                destination = destination - self.width // 2

            if self.x < mouse[MOUSE_POS_X]:
                self.setPath(destination)
            elif self.x > mouse[MOUSE_POS_X]:
                self.setPath(destination)

        #keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP] and self.y > self.upY:
        #     self.move_ip(0, -self.speed)
        #     self.goingLeft = False
        #     self.goingRight = False
        # if keys[pygame.K_DOWN] and self.y < self.downY:
        #     self.move_ip(0, +self.speed)
        #     self.goingLeft = False
        #     self.goingRight = False
        # if keys[pygame.K_LEFT] and self.x > self.leftWallX:
        #     self.move_ip(-self.speed, 0)
        #     self.goingLeft = True
        #     self.goingRight = False
        # elif keys[pygame.K_RIGHT] and self.x < self.rightWallX - self.width:
        #     self.move_ip(+self.speed, 0)
        #     self.goingLeft = False
        #     self.goingRight = True
        # else:
        #     self.goingLeft = False
        #     self.goingRight = False
        #     self.walkCount = 0

    def moveToDestination(self):
        if self.x < self.destination:
            if self.destination - self.x < self.speed:
                self.move_ip((self.destination - self.x), 0)
            else:
                self.move_ip(+self.speed, 0)
            self.goingLeft = False
            self.goingRight = True
        elif self.x > self.destination:
            if self.x - self.destination < self.speed:
                self.move_ip((self.destination - self.x), 0)
            else:
                self.move_ip(-self.speed, 0)
            self.goingLeft = True
            self.goingRight = False
        if self.x == self.destination:
            self.moving = False
            self.goingLeft = False
            self.goingRight = False
            self.walkCount = 0

    def setConstraints(self, constraints):
        self.constraints = self.leftWallX, self.rightWallX, self.downY, self.upY = constraints
        # self.leftWallX += self.width // 2
        self.rightWallX -= self.width // 2

    def setPath(self, destination):
        self.destination = destination
        self.moving = True

    def getPath(self):
        return self.destination

    def setHealth(self, health):
        self.health = health
        self.statusChanged = True

    def getHealth(self):
        return self.health

    def setMentality(self, mentality):
        self.mentality = mentality
        self.statusChanged = True

    def getMentality(self):
        return self.mentality

    def setWeapon(self, weapon):
        self.weapon = weapon
        self.statusChanged = True

    def getWeapon(self):
        return self.weapon

    def setConsumable(self, consumable):
        self.consumable = consumable
        self.statusChanged = True

    def getConsumable(self):
        return self.consumable

    def setExperience(self, experience):
        self.experience = experience
        self.statusChanged = True

    def getExperience(self):
        return self.experience

