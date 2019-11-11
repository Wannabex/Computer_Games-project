import pygame


class Building(pygame.Rect):
    def __init__(self, screen, screenSize):
        self.screenWidth, self.screenHeight = screenSize
        self.constraints = self.leftWallX, self.rightWallX, self.floorY, self.ceilingY = 125, self.screenWidth - 125, self.screenHeight - 40, 100
        pygame.Rect.__init__(self, (self.leftWallX, self.ceilingY, self.rightWallX - self.leftWallX, self.floorY - self.ceilingY))
        self.screen = screen
        print("xWidth buildinga to " + str(self.x + self.width) + "yHeight to " + str(self.y + self.height))

    def update(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self)
        #self.screen.blit(self.surf, self)

    def getWalls(self):
        return self.constraints