import pygame

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

WHEEL_IDLE = 1
WHEEL_HOVER = 0

class Interface(object):
    def __init__(self, screen, screenX, screenY):
        self.score = InterfacePart(screen, 3, 3, "Score: ", "0")
        self.time = InterfacePart(screen, screenX - 110, 3, "Time: ", "22:00")
        self.equipment1 = InterfacePart(screen, screenX//2 - 175, screenY - 28, "Weapon: ", "Nothing")
        self.equipment2 = InterfacePart(screen, screenX//2 + 75, screenY - 28, "Consumable: ", "Nothing")
        self.health = InterfacePart(screen, 3, screenY - 28, "Health: ", "", (204, 0, 0))
        self.healthBar = StatusIndicator(screen, 3, screenY - 34, 128, 50, (204, 0, 0))
        self.mentality = InterfacePart(screen, screenX - 160, screenY - 28, "Mentality: ", "", (0, 153, 255))
        self.mentalityBar = StatusIndicator(screen, screenX - 160, screenY - 34, 153, 30, (0, 153, 255))

    def update(self):
        self.score.update()
        self.time.update()
        self.equipment1.update()
        self.equipment2.update()
        self.health.update()
        self.healthBar.update()
        self.mentality.update()
        self.mentalityBar.update()


class InterfacePart(pygame.Rect):
    def __init__(self, screen, positionX, positionY, indicator, information, color = (255, 255, 255)):
        pygame.Rect.__init__(self, (positionX, positionY, 100, 20))
        self.indicator = indicator
        self.information = information
        self.color = color
        self.screen = screen
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 18)
        self.surf = self.font.render((self.indicator + self.information), True, self.color)

    def update(self):
        self.screen.blit(self.surf, self)

    def setInformation(self, information):
        self.information = information
        self.surf = self.font.render((self.indicator + self.information), True, self.color)


class StatusIndicator(pygame.Rect):
    def __init__(self, screen, positionX, positionY, barWidth, value, color = (255, 255, 255)):
        self.screen = screen
        self.maxValue = 100
        self.ratio = barWidth / self.maxValue
        self.value = value
        self.width = self.value * self.ratio
        self.color = color
        pygame.Rect.__init__(self, (positionX, positionY, self.width, 5))
        self.statusBar = pygame.Rect((positionX - 1, positionY - 1, barWidth + 2, 7))

    def update(self):
        pygame.draw.rect(self.screen, (0,0,0), self.statusBar)
        pygame.draw.rect(self.screen, self.color, self)

    def setValue(self, value):
        self.value = value
        self.width = self.value * self.ratio

    def getValue(self):
        return self.value


class ActionWheel(pygame.Rect):
    WHEEL_WIDTH = 48
    WHEEL_HEIGHT = 48

    wheelCancel = [pygame.image.load("./resources/images/wheel/cancel1.png"),
                   pygame.image.load("./resources/images/wheel/cancel2.png")]
    wheelInspect = [pygame.image.load("./resources/images/wheel/inspect1.png"),
                   pygame.image.load("./resources/images/wheel/inspect2.png")]
    wheelTake = [pygame.image.load("./resources/images/wheel/take1.png"),
                   pygame.image.load("./resources/images/wheel/take2.png")]

    def __init__(self, screen, hero, object, weapon=0, consumable=0, takeable=True):
        self.screen = screen
        self.hero = hero
        self.interfacedObject = object
        self.positionX = object.x - self.WHEEL_WIDTH + 3
        self.positionY = object.y - self.WHEEL_HEIGHT + 3
        pygame.Rect.__init__(self, (self.positionX, self.positionY, self.WHEEL_WIDTH, self.WHEEL_HEIGHT))
        self.optionWidth = 16
        self.optionHeight = 16
        self.optionUp = pygame.Rect((self.positionX + self.optionWidth, self.positionY, self.optionWidth, self.optionHeight))
        self.optionLeft = pygame.Rect((self.positionX, self.positionY + self.optionHeight, self.optionWidth, self.optionHeight))
        self.optionMiddle = pygame.Rect((self.positionX + self.optionWidth, self.positionY + self.optionHeight, self.optionWidth, self.optionHeight))
        self.optionRight = pygame.Rect((self.positionX + 2 * self.optionWidth, self.positionY + self.optionHeight, self.optionWidth, self.optionHeight))
        self.optionDown = pygame.Rect((self.positionX + self.optionWidth, self.positionY + 2 * self.optionHeight, self.optionWidth, self.optionHeight))
        self.upIcon = self.wheelInspect[WHEEL_IDLE]
        self.leftIcon = 0
        self.middleIcon = self.wheelCancel[WHEEL_IDLE]
        self.rightIcon = 0
        self.downIcon = 0
        if takeable:
            self.downIcon = self.wheelTake[WHEEL_IDLE]
        if weapon != 0:
            self.wheelWeapon = weapon
            self.leftIcon = self.wheelWeapon[WHEEL_IDLE]
        if consumable != 0:
            self.wheelConsumable = consumable
            self.rightIcon = self.wheelConsumable[WHEEL_IDLE]
        self.upClicked = False
        self.leftClicked = False
        self.middleClicked = False
        self.rightClicked = False
        self.downClicked = False
        self.descriptionVisible = False

    def update(self):
        self.wheelControl()
        if self.upIcon != 0:
            self.screen.blit(self.upIcon, self.optionUp)
        if self.leftIcon != 0:
            self.screen.blit(self.leftIcon, self.optionLeft)
        if self.middleIcon != 0:
            self.screen.blit(self.middleIcon, self.optionMiddle)
        if self.rightIcon != 0:
            self.screen.blit(self.rightIcon, self.optionRight)
        if self.downIcon != 0:
            self.screen.blit(self.downIcon, self.optionDown)
        if self.upClicked:
            pygame.draw.rect(self.screen, (0, 0, 0), self.descriptionRect)
            self.screen.blit(self.descriptionText, self.descriptionRect)

    def wheelControl(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()

        if self.upIcon != 0:
            self.upIcon = self.wheelInspect[WHEEL_IDLE]
        if self.leftIcon != 0:
            self.leftIcon = self.wheelWeapon[WHEEL_IDLE]
        if self.middleIcon != 0:
            self.middleIcon = self.wheelCancel[WHEEL_IDLE]
        if self.rightIcon != 0:
            self.rightIcon = self.wheelConsumable[WHEEL_IDLE]
        if self.downIcon != 0:
            self.downIcon = self.wheelTake[WHEEL_IDLE]

        if self.optionUp.x <= mouse[MOUSE_POS_X] <= self.optionUp.x + self.optionUp.width and self.optionUp.y <= mouse[MOUSE_POS_Y] <= self.optionUp.y + self.optionUp.height:
            self.upIcon = self.wheelInspect[WHEEL_HOVER]
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.upClicked = True
                self.showInterfacedObjectDescritpion()
        elif self.leftIcon and self.optionLeft.x <= mouse[MOUSE_POS_X] <= self.optionLeft.x + self.optionLeft.width and self.optionLeft.y <= mouse[MOUSE_POS_Y] <= self.optionLeft.y + self.optionLeft.height:
            self.leftIcon = self.wheelWeapon[WHEEL_HOVER]
            self.leftClicked = True
            self.middleClicked = True
            self.hero.destinationEnemy = self.interfacedObject
            self.hero.setPath(self.interfacedObject.x, self.interfacedObject.y)
        elif self.optionMiddle.x <= mouse[MOUSE_POS_X] <= self.optionMiddle.x + self.optionMiddle.width and self.optionMiddle.y <= mouse[MOUSE_POS_Y] <= self.optionMiddle.y + self.optionMiddle.height:
            self.middleIcon = self.wheelCancel[WHEEL_HOVER]
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.middleClicked = True
                self.upClicked = False
        elif self.rightIcon and self.optionRight.x <= mouse[MOUSE_POS_X] <= self.optionRight.x + self.optionRight.width and self.optionRight.y <= mouse[MOUSE_POS_Y] <= self.optionRight.y + self.optionRight.height:
            self.rightIcon = self.wheelConsumable[WHEEL_HOVER]
        elif self.downIcon and self.optionDown.x <= mouse[MOUSE_POS_X] <= self.optionDown.x + self.optionDown.width and self.optionDown.y <= mouse[MOUSE_POS_Y] <= self.optionDown.y + self.optionDown.height:
            self.downIcon = self.wheelTake[WHEEL_HOVER]
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.downClicked = True
                self.middleClicked = True
                self.hero.destinationEquipment = self.interfacedObject
                self.hero.setPath(self.interfacedObject.x, self.interfacedObject.y)

        elif self.upClicked and self.descriptionRect.x <= mouse[MOUSE_POS_X] <= self.descriptionRect.x + self.descriptionRect.width and self.descriptionRect.y <= mouse[MOUSE_POS_Y] <= self.descriptionRect.y + self.descriptionRect.height:
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.upClicked = False

    def wheelEvents(self):
        if self.upClicked:
            return 0
        if self.leftClicked:
            return 1
        if self.middleClicked:
            return 2
        if self.rightClicked:
            return 3
        if self.downClicked:
            return 4

    def showInterfacedObjectDescritpion(self):
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 12)
        self.descriptionText = self.font.render(self.interfacedObject.description, True, (255, 255, 255))
        descriptionWidth = len(self.interfacedObject.description) * 7
        descriptionHeight = 20
        self.descriptionRect = pygame.Rect((self.positionX + 50, self.positionY, descriptionWidth, descriptionHeight))

