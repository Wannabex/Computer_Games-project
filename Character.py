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

    walkLeft = ["./resources/character/L1.png", "./resources/character/L2.png", "./resources/character/L3.png",
                "./resources/character/L4.png", "./resources/character/L5.png", "./resources/character/L6.png",
                "./resources/character/L7.png", "./resources/character/L8.png", "./resources/character/L9.png"]

    walkRight = ["./resources/character/R1.png", "./resources/character/R2.png", "./resources/character/R3.png",
                 "./resources/character/R4.png", "./resources/character/R5.png", "./resources/character/R6.png",
                 "./resources/character/R7.png", "./resources/character/R8.png", "./resources/character/R9.png"]
    stay = "./resources/character/standing.png"

    def __init__(self, screen, positionX, positionY):
        pygame.Rect.__init__(self, (positionX, positionY, CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.screen = screen
        self.playerImage = pygame.image.load(self.stay)
        self.characterSpeed = 5
        self.goingLeft = False
        self.goingRight = False
        self.moving = False
        self.walkCount = 0
        self.health = random.randint(30, 70)
        self.mentality = 30 + 70 - self.health
        self.weapon = "Hands"
        self.usable = "Bread"
        self.experience = 0

    def update(self):
        self.screen.blit(self.playerImage, self)

    def animation(self):
        if self.goingLeft:
            self.playerImage = pygame.image.load(self.walkLeft[self.walkCount//3])
            self.walkCount += 1
        elif self.goingRight:
            self.playerImage = pygame.image.load(self.walkRight[self.walkCount // 3])
            self.walkCount += 1
        else:
            self.playerImage = pygame.image.load(self.stay)
        self.walkCount %= 27

    def control(self):
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pos()
        #print(mouse)
        #print(type(mouse)) tuple
        mouseClick = pygame.mouse.get_pressed()
        #print(mouseClick)
        #print(type(mouseClick)) tuple

        if mouseClick[MOUSE_BUTTON_LEFT] and self.leftWallX <= mouse[MOUSE_POS_X] <= self.rightWallX:
            print("JESTEM TUTAJ")

        if keys[pygame.K_UP] and self.y > self.upY:
            self.move_ip(0, -self.characterSpeed)
            self.goingLeft = False
            self.goingRight = False
        if keys[pygame.K_DOWN] and self.y < self.downY:
            self.move_ip(0, +self.characterSpeed)
            self.goingLeft = False
            self.goingRight = False
        if keys[pygame.K_LEFT] and self.x > self.leftWallX:
            self.move_ip(-self.characterSpeed, 0)
            self.goingLeft = True
            self.goingRight = False
        elif keys[pygame.K_RIGHT] and self.x < self.rightWallX - self.width:
            self.move_ip(+self.characterSpeed, 0)
            self.goingLeft = False
            self.goingRight = True
        else:
            self.goingLeft = False
            self.goingRight = False
            self.walkCount = 0

    def moveToDestination(self, destination):
        pass

    def setConstraints(self, constraints):
        self.constraints = self.leftWallX, self.rightWallX, self.downY, self.upY = constraints
        self.downY =  self.downY - self.height - 3

    def setPath(self, destination):
        self.destination = destination
        self.moving = True

    def getPath(self):
        return self.destination

    def setHealth(self, health):
        self.health = health

    def getHealth(self):
        return self.health

    def setMentality(self, mentality):
        self.mentality = mentality

    def getMentality(self):
        return self.mentality

    def setWeapon(self, weapon):
        self.weapon = weapon

    def getWeapon(self):
        return self.weapon

    def setUsable(self, usable):
        self.usable = usable

    def getUsable(self):
        return self.usable

    def setExperience(self, experience):
        self.experience = experience

    def getExperience(self):
        return self.experience

