import pygame

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

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

    def __init__(self, screen, positionX, positionY, weapon=0, consumable=0):
        self.screen = screen
        pygame.Rect.__init__(self, (positionX, positionY, self.WHEEL_WIDTH, self.WHEEL_HEIGHT))
        self.optionWidth = 16
        self.optionHeight = 16
        self.optionUp = pygame.Rect((positionX + self.optionWidth, positionY, self.optionWidth, self.optionHeight))
        self.optionLeft = pygame.Rect((positionX, positionY + self.optionHeight, self.optionWidth, self.optionHeight))
        self.optionMiddle = pygame.Rect((positionX + self.optionWidth, positionY + self.optionHeight, self.optionWidth, self.optionHeight))
        self.optionRight = pygame.Rect((positionX + 2 * self.optionWidth, positionY + self.optionHeight, self.optionWidth, self.optionHeight))
        self.optionDown = pygame.Rect((positionX + self.optionWidth, positionY + 2 * self.optionHeight, self.optionWidth, self.optionHeight))
        self.upIcon = 0
        self.leftIcon = 0
        self.middleIcon = 0
        self.rightIcon = 0
        self.downIcon = 0
        self.weapon = weapon
        self.consumable = consumable
        self.upClicked = False
        self.leftClicked = False
        self.middleClicked = False
        self.rightClicked = False
        self.downClicked = False

    def setActionWheel(self, upIcon=0, leftIcon=0, middleIcon=0, rightIcon=0, downIcon=0):
        if upIcon != 0:
            self.upIcon = upIcon
        if leftIcon != 0:
            self.leftIcon = leftIcon
        if middleIcon != 0:
            self.middleIcon = middleIcon
        if rightIcon != 0:
            self.rightIcon = rightIcon
        if downIcon != 0:
            self.downIcon = downIcon

    def update(self):
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


    def wheelControl(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        #if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:


