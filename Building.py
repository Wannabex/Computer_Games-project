import pygame
import random
import Trash

class Building(pygame.Rect):
    def __init__(self, screen, screenSize):
        self.screenWidth, self.screenHeight = screenSize
        self.constraints = self.leftWallX, self.rightWallX, self.floorY, self.ceilingY = 125, self.screenWidth - 125, self.screenHeight - 40, 100
        pygame.Rect.__init__(self, (self.leftWallX, self.ceilingY, self.rightWallX - self.leftWallX, self.floorY - self.ceilingY))
        self.screen = screen
        print(self.rightWallX - self.x)
        print(self.floorY - self.y)
        self.manor = pygame.image.load("./resources/images/gameboard/manor3.png")
        self.floor3Y = self.ceilingY + 208
        self.floor2Y = self.ceilingY + 461
        self.floor1Y = self.ceilingY + 637
        self.floorsYs = [self.floor3Y, self.floor2Y, self.floor1Y, self.floor1Y]
        self.floor1LeftColumnX = self.leftWallX + 663
        self.floor1RightColumnX = self.leftWallX + 1014
        self.stoneDoor1X = self.leftWallX + 225 #Floor1
        self.stoneDoor2X = self.leftWallX + 1050 #Floor1
        self.stoneDoorWidth = 65
        self.woodenDoor1X = self.leftWallX + 1166 #Floor1
        self.woodenDoor2X = self.leftWallX + 222 #Floor2
        self.woodenDoorWidth = 41
        self.oldDoor1X = self.leftWallX + 623 #Floor2
        self.oldDoor2X = self.leftWallX + 972 #Floor3
        self.oldDoorWidth = 36
        self.doorsX = [self.stoneDoor1X, self.stoneDoor2X, self.woodenDoor1X, self.woodenDoor2X, self.oldDoor1X, self.oldDoor2X]
        self.doorsWidth = [self.stoneDoorWidth,self.stoneDoorWidth, self.woodenDoorWidth, self.woodenDoorWidth, self.oldDoorWidth, self.oldDoorWidth]
        self.currentlySpawned = []

    def update(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self)
        self.screen.blit(self.manor, self)

    def getWalls(self):
        return self.constraints

    def spawnObject(self, object):
        self.objectPositionSelect(object)
        self.checkFreePositions(object)
        self.currentlySpawned.append(object)

    def objectPositionSelect(self, object):
        if not type(object) == Trash.Angel:
            object.y = random.choice(self.floorsYs) - object.height
        else:
            object.y = random.choice(self.floorsYs[:2]) - object.height
        if not (object.y == self.floor1Y - object.height):
            object.x = random.randint(self.leftWallX, self.rightWallX - object.width)
        else:
            side = random.randint(1, 2)
            if side == 1:
                object.x = random.randint(self.leftWallX, self.floor1LeftColumnX - object.width)
            else:
                object.x = random.randint(self.floor1RightColumnX, self.rightWallX - object.width)

    def checkFreePositions(self, object):
        if len(self.currentlySpawned) > 1:
            xOccupied = []
            xWidthOccupied = []
            for spawned in self.currentlySpawned:
                xOccupied.append(spawned.x - object.width - 5)
                xWidthOccupied.append(spawned.x + spawned.width + object.width + 5)
            xConditionChecked = []
            for currentlyChecked in range(len(xOccupied)):
                xConditionChecked.append(xWidthOccupied[currentlyChecked] <= object.x or object.x <= xOccupied[currentlyChecked])
            while not all(xConditionChecked):
                self.objectPositionSelect(object)
                xConditionChecked = []
                for currentlyChecked in range(len(xOccupied)):
                    xConditionChecked.append(xWidthOccupied[currentlyChecked] <= object.x or object.x <= xOccupied[currentlyChecked])



    # def checkFreePositions(self, object, items, enemies):
    #     currentlySpawned = []
    #     for item in items:
    #         currentlySpawned.append(item)
    #     for enemy in enemies:
    #         currentlySpawned.append(enemy)
    #     xOccupied = []
    #     xWidthOccupied = []
    #     yOccupied = []
    #     yHeightOccupied = []
    #     for spawned in currentlySpawned:
    #         xOccupied.append(spawned.x - object.width - 10)
    #         xWidthOccupied.append(spawned.x + spawned.width + object.width + 10)
    #         yOccupied.append(spawned.y - object.height - 10)
    #         yHeightOccupied.append(spawned.y + spawned.height + object.height + 10)
    #
    #     xConditionChecked = []
    #     yConditionChecked = []
    #     for currentlyChecked in range(len(xOccupied)):
    #         xConditionChecked.append(xWidthOccupied[currentlyChecked] <= object.x or object.x <= xOccupied[currentlyChecked])
    #     for currentlyChecked in range(len(yOccupied)):
    #         yConditionChecked.append(yHeightOccupied[currentlyChecked] <= object.y or object.y <= yOccupied[currentlyChecked])
    #     while not all(xConditionChecked) and not all(yConditionChecked):
    #         object.x = random.randint(self.building.leftWallX, self.building.rightWallX - object.width)
    #         object.y = random.randint(self.building.ceilingY, self.building.floorY - object.height - 3)
    #         xConditionChecked = []
    #         yConditionChecked = []
    #         for currentlyChecked in range(len(xOccupied)):
    #             xConditionChecked.append(xWidthOccupied[currentlyChecked] <= object.x or object.x <= xOccupied[currentlyChecked])
    #         for currentlyChecked in range(len(yOccupied)):
    #             yConditionChecked.append(yHeightOccupied[currentlyChecked] <= object.y or object.y <= yOccupied[currentlyChecked]),
