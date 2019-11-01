import pygame

class Interface(pygame.Rect):
    def __init__(self, screen, screenX, screenY):
        self.score = Score(screen)
        self.equipment = Equipment(screen, screenX, screenY)
        self.health = Health(screen, screenX, screenY)

    def update(self):
        self.score.update()
        self.equipment.update()
        self.health.update()



class Score(pygame.Rect):
        def __init__(self, screen):
            self.positionX = 0
            self.positionY = 0
            self.width = 30
            self.height = 30
            self.text = "Score"
            self.color = (0, 0, 0)
            self.screen = screen
            self.information = pygame.font.Font(None, 20)
            self.surf = self.information.render(self.text, 1, self.color)
            self.rect = self.screen.get_rect(center=(self.positionX, self.positionY))

        def update(self):
            self.screen.blit(self.screen, self.rect)


class Equipment(pygame.Rect):
    def __init__(self, screen, screenX, screenY):
        self.positionX = screenX
        self.positionY = screenY - 30
        self.width = 30
        self.height = 30
        self.text = "Weapon     Usable"
        self.color = (0, 0, 0)
        self.screen = screen
        self.information = pygame.font.Font(None, 20)
        self.surf = self.information.render(self.text, 1, self.color)
        self.rect = self.screen.get_rect(center=(self.positionX, self.positionY))

    def update(self):
        self.screen.blit(self.screen, self.rect)


class Health(pygame.Rect):
    def __init__(self, screen, screenX, screenY):
        self.positionX = screenX
        self.positionY = screenY
        self.width = 30
        self.height = 30
        self.text = "Health     Stress"
        self.color = (255, 0, 0)
        self.screen = screen
        self.information = pygame.font.Font(None, 20)
        self.surf = self.information.render(self.text, 1, self.color)
        self.rect = self.screen.get_rect(center=(self.positionX, self.positionY))

    def update(self):
        self.screen.blit(self.surf, self.rect)