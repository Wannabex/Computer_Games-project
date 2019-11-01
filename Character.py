import pygame


class Player(pygame.Rect):

    walkLeft = ["./resources/character/L1.png", "./resources/character/L2.png", "./resources/character/L3.png",
                "./resources/character/L4.png", "./resources/character/L5.png", "./resources/character/L6.png",
                "./resources/character/L7.png", "./resources/character/L8.png", "./resources/character/L9.png"]

    walkRight = ["./resources/character/R1.png", "./resources/character/R2.png", "./resources/character/R3.png",
                 "./resources/character/R4.png", "./resources/character/R5.png", "./resources/character/R6.png",
                 "./resources/character/R7.png", "./resources/character/R8.png", "./resources/character/R9.png"]
    stay = "./resources/character/standing.png"

    def __init__(self):
        positionX, positionY, characterWidth, characterHeight = 0, 0, 64, 64
        pygame.Rect.__init__(self, (positionX, positionY, characterWidth, characterHeight))
        self.playerImage = pygame.image.load(self.stay)

        self.characterSpeed = 5
        self.goingLeft = False
        self.goingRight = False
        self.walkCount = 0

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


