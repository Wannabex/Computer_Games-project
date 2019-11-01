import pygame


class Interface(object):
    def __init__(self, screen, screenX, screenY):
        self.score = InterfacePart(screen, 3, 3, "Score: 0")
        self.time = InterfacePart(screen, screenX - 80, 3, "Time: 22:00")
        self.equipment = InterfacePart(screen, screenX - 600, screenY - 20, "Weapon: Sword   Usable: Molotov")
        self.health = InterfacePart(screen, screenX - 220, screenY - 20, "Health: 50/100     Mentality: 30/100")

    def update(self):
        self.score.update()
        self.time.update()
        self.equipment.update()
        self.health.update()

class InterfacePart(pygame.Rect):
    def __init__(self, screen, positionX, positionY, information):
        pygame.Rect.__init__(self, (positionX, positionY, 100, 50))
        self.text = information
        self.color = (255, 255, 255)
        self.screen = screen
        self.information = pygame.font.Font(None, 20)
        self.surf = self.information.render(self.text, 1, self.color)

    def update(self):
        self.screen.blit(self.surf, self)

