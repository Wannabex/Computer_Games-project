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
    def __init__(self, screen, positionX, positionY, weapon, consumable):
        self.width = 48
        self.height = 48
        pygame.Rect.__init__(self, (positionX, positionY, self.width, self.height))
        self.weapon = weapon
        self.consumable = consumable
        # if optionsCount == 1
        #     self.options.append(pygame.Rect((positionX - 1, positionY - 1, barWidth + 2, 7)))


    def update(self):
        pass

        # mouse = pygame.mouse.get_pos()
        # mouseClick = pygame.mouse.get_pressed()
        # if self.playRect.x <= mouse[MOUSE_POS_X] <= self.playRect.x + self.playRect.width and self.playRect.y <= mouse[MOUSE_POS_Y] <= self.playRect.y + self.playRect.height:
        #     self.playRectColor = self.BROWN
        #     if mouseClick[MOUSE_BUTTON_LEFT]:
        #         self.playActivated = True

