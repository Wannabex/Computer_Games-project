import pygame


class Interface(object):
    def __init__(self, screen, screenX, screenY):
        self.score = InterfacePart(screen, 3, 3, "Score: ", "0")
        self.time = InterfacePart(screen, screenX - 110, 3, "Time: ", "22:00")
        self.equipment1 = InterfacePart(screen, screenX//2 - 100, screenY - 26, "Weapon: ", "Hands")
        self.equipment2 = InterfacePart(screen, screenX//2 + 100, screenY - 26, "Usable: ", "Bread")
        self.health = InterfacePart(screen, 3, screenY - 26, "Health: ", "50/100", (204, 0, 0))
        self.healthBar = StatusIndicator(screen, 3, screenY - 30, 130, 50, (204, 0, 0))
        self.mentality = InterfacePart(screen, screenX - 160, screenY - 26, "Mentality: ", "30/100", (0, 0, 102))
        self.mentalityBar = StatusIndicator(screen, screenX - 160, screenY - 34, 155, 30, (0, 0, 102))

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
        print(self.ratio)
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