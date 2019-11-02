import pygame


class Player(pygame.Rect):

    walkLeft = ["./resources/character/L1.png", "./resources/character/L2.png", "./resources/character/L3.png",
                "./resources/character/L4.png", "./resources/character/L5.png", "./resources/character/L6.png",
                "./resources/character/L7.png", "./resources/character/L8.png", "./resources/character/L9.png"]

    walkRight = ["./resources/character/R1.png", "./resources/character/R2.png", "./resources/character/R3.png",
                 "./resources/character/R4.png", "./resources/character/R5.png", "./resources/character/R6.png",
                 "./resources/character/R7.png", "./resources/character/R8.png", "./resources/character/R9.png"]
    stay = "./resources/character/standing.png"

    def __init__(self, positionX, positionY):
        pygame.Rect.__init__(self, (positionX, positionY, 64, 64))
        self.playerImage = pygame.image.load(self.stay)
        self.characterSpeed = 5
        self.goingLeft = False
        self.goingRight = False
        self.walkCount = 0
        self.health = 50
        self.mentality = 30
        self.weapon = "Hands"
        self.usable = "Bread"
        self.experience = 0

    def setConstraints(self, constraints):
        self.constraints = self.leftX, self.rightX, self.downY, self.upY = constraints

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
        if keys[pygame.K_UP] and self.y > self.upY:
            self.move_ip(0, -self.characterSpeed)
            self.goingLeft = False
            self.goingRight = False
        if keys[pygame.K_DOWN] and self.y < self.downY:
            self.move_ip(0, +self.characterSpeed)
            self.goingLeft = False
            self.goingRight = False
        if keys[pygame.K_LEFT] and self.x > self.leftX:
            self.move_ip(-self.characterSpeed, 0)
            self.goingLeft = True
            self.goingRight = False
        elif keys[pygame.K_RIGHT] and self.x < self.rightX - self.width:
            self.move_ip(+self.characterSpeed, 0)
            self.goingLeft = False
            self.goingRight = True
        else:
            self.goingLeft = False
            self.goingRight = False
            self.walkCount = 0


