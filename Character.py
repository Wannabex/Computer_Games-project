import pygame
import random
import Equipment
import Interface

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

    def __init__(self, screen, positionX, positionY, screenX, screenY):
        pygame.Rect.__init__(self, (positionX, positionY, CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.screen = screen
        self.interface = Interface.Interface(screen, screenX, screenY)
        self.playerImage = self.stay
        self.speed = 5
        self.goingLeft = False
        self.goingRight = False
        self.moving = False
        self.walkCount = 0
        self.setHealth(random.randint(30, 70))
        self.setMentality(30 + 70 - self.health)
        self.weapon = "Nothing"
        self.consumable = "Nothing"
        self.experience = 0
        self.time = "22:00"

    def update(self):
        self.animation()
        if self.moving:
            self.moveToDestination()
        self.screen.blit(self.playerImage, self)
        self.interface.update()

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
        if mouseClick[MOUSE_BUTTON_RIGHT] and self.leftWallX <= mouse[MOUSE_POS_X] <= self.rightWallX + self.width // 2:
            destination = mouse[MOUSE_POS_X] - self.width // 2
            if self.leftWallX - self.width // 2 <= destination <= self.leftWallX:
                destination = destination + self.width // 2
            elif self.rightWallX - self.width // 2 <= destination <= self.rightWallX:
                destination = destination - self.width // 2
            if self.x < mouse[MOUSE_POS_X]:
                self.setPath(destination)
            elif self.x > mouse[MOUSE_POS_X]:
                self.setPath(destination)

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

    def setHealth(self, newHealth):
        self.health = newHealth
        self.interface.health.setInformation(str(newHealth) + "/100")
        self.interface.healthBar.setValue(int(newHealth))

    def getHealth(self):
        return self.health

    def setMentality(self, newMentality):
        self.mentality = newMentality
        self.interface.mentality.setInformation(str(newMentality) + "/100")
        self.interface.mentalityBar.setValue(int(newMentality))

    def getMentality(self):
        return self.mentality

    def setWeapon(self, newWeapon):
        self.weapon = newWeapon.getName()
        newWeapon.pickUp(self.interface.equipment1.x - Equipment.ICON_WIDTH - 3, self.interface.equipment1.y - 5)
        self.interface.equipment1.setInformation(self.weapon)

    def getWeapon(self):
        return self.weapon

    def setConsumable(self, newConsumable):
        self.consumable = newConsumable.getName()
        newConsumable.pickUp(self.interface.equipment2.x - Equipment.ICON_WIDTH - 3, self.interface.equipment1.y - 5)
        self.interface.equipment2.setInformation(self.consumable)

    def getConsumable(self):
        return self.consumable

    def setExperience(self, newExperience):
        self.experience = newExperience
        self.interface.score.setInformation(str(newExperience))

    def getExperience(self):
        return self.experience

    def setTime(self, newTime):
        self.time = newTime
        self.interface.time.setInformation(str(newTime))

    def getTime(self):
        return self.time

