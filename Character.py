import pygame

walkRight = [pygame.image.load("./resources/character/L1.png"), pygame.image.load("./resources/character/L2.png"), pygame.image.load("./resources/character/L3.png"),
             pygame.image.load("./resources/character/L4.png"), pygame.image.load("./resources/character/L5.png"), pygame.image.load("./resources/character/L6.png"),
             pygame.image.load("./resources/character/L7.png"), pygame.image.load("./resources/character/L8.png"), pygame.image.load("./resources/character/L9.png")]
walkLeft = [pygame.image.load("./resources/character/R1.png"), pygame.image.load("./resources/character/R2.png"), pygame.image.load("./resources/character/R3.png"),
            pygame.image.load("./resources/character/R4.png"), pygame.image.load("./resources/character/R5.png"), pygame.image.load("./resources/character/R6.png"),
            pygame.image.load("./resources/character/R7.png"), pygame.image.load("./resources/character/R8.png"), pygame.image.load("./resources/character/R9.png")]
stay = pygame.image.load("./resources/character/standing.png")

class Player(pygame.Rect):
    def __init__(self):
        characterX, characterY, characterWidth, characterHeight = 0, 0, 34, 34
        pygame.Rect.__init__(self, characterX, characterY, characterWidth, characterHeight)
        self.characterSpeed = 9
