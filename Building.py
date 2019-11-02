import pygame


class Building(pygame.Rect):
    def __init__(self, screen, screenSize):
        self.screenWidth, self.screenHeight = screenSize
        self.constraints = self.leftWallX, self.rightWallX, self.floorY, self.ceilingY = 100, 850, self.screenHeight - 95, 100
        pygame.Rect.__init__(self, (self.leftWallX, self.ceilingY, self.rightWallX - self.leftWallX, self.floorY - self.ceilingY))
        self.screen = screen

    def update(self):
        pass

    def getWalls(self):
        return self.constraints