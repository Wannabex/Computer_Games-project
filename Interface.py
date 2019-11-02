import pygame


class Interface(object):
    def __init__(self, screen, screenX, screenY):
        self.score = InterfacePart(screen, 3, 3, "Score: ", "0")
        self.time = InterfacePart(screen, screenX - 115, 3, "Time: ", "22:00")
        self.equipment1 = InterfacePart(screen, screenX - 630, screenY - 26, "Weapon: ", "Hands")
        self.equipment2 = InterfacePart(screen, screenX - 450, screenY - 26, "Usable: ", "Bread")
        self.health = InterfacePart(screen, 3, screenY - 26, "Health: ", "50/100", (204, 0, 0))
        self.mentality = InterfacePart(screen, screenX - 170, screenY - 26, "Mentality: ", "30/100", (0, 0, 102))

    def update(self):
        self.score.update()
        self.time.update()
        self.equipment1.update()
        self.equipment2.update()
        self.health.update()
        self.mentality.update()

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