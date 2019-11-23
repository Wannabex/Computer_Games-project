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
        # manor2.png settings - fullHD resolution
        # self.floor3Y = self.ceilingY + 208
        # self.floor2Y = self.ceilingY + 461
        # self.floor1Y = self.ceilingY + 637
        # self.floorsYs = [self.floor3Y, self.floor2Y, self.floor1Y, self.floor1Y]
        # self.floor1LeftColumnX = self.leftWallX + 663
        # self.floor1RightColumnX = self.leftWallX + 1014
        # self.stoneDoor1X = self.leftWallX + 225 #Floor1
        # self.stoneDoor2X = self.leftWallX + 1050 #Floor1
        # self.stoneDoorWidth = 65
        # self.woodenDoor1X = self.leftWallX + 1166 #Floor1
        # self.woodenDoor2X = self.leftWallX + 222 #Floor2
        # self.woodenDoorWidth = 41
        # self.oldDoor1X = self.leftWallX + 623 #Floor2
        # self.oldDoor2X = self.leftWallX + 972 #Floor3
        # self.oldDoorWidth = 36

        # manor3.png settings = HD resolution
        self.floor3Y = self.ceilingY + 192
        self.floor2Y = self.ceilingY + 420
        self.floor1Y = self.ceilingY + 579
        self.floorsYs = [self.floor3Y, self.floor2Y, self.floor1Y, self.floor1Y]
        self.floor1LeftColumnX = self.leftWallX + 582
        self.floor1RightColumnX = self.leftWallX + 892
        self.stoneDoor1X = self.leftWallX + 187  #Floor1
        self.stoneDoor2X = self.leftWallX + 910 #Floor1
        self.stoneDoorWidth = 65
        self.woodenDoor1X = self.leftWallX + 1024 #Floor1
        self.woodenDoor2X = self.leftWallX + 193 #Floor2
        self.woodenDoorWidth = 36
        self.oldDoor1X = self.leftWallX + 547 #Floor2
        self.oldDoor2X = self.leftWallX + 854 #Floor3
        self.oldDoorWidth = 33
        self.doorsPositions = {self.floor1Y: {self.stoneDoor1X: self.stoneDoorWidth, self.stoneDoor2X: self.stoneDoorWidth, self.woodenDoor1X: self.woodenDoorWidth},
                              self.floor2Y: {self.woodenDoor2X: self.woodenDoorWidth, self.oldDoor1X: self.oldDoorWidth},
                              self.floor3Y: {self.oldDoor2X: self.oldDoorWidth}}

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

            # self.doorsPositions = {
            #     self.floor1Y: {self.stoneDoor1X: self.stoneDoorWidth, self.stoneDoor2X: self.stoneDoorWidth,
            #                    self.woodenDoor1X: self.woodenDoorWidth},
            #     self.floor2Y: {self.woodenDoor2X: self.woodenDoorWidth, self.oldDoor1X: self.oldDoorWidth},
            #     self.floor3Y: {self.oldDoor2X: self.oldDoorWidth}}
            xConditionChecked = []
            doorsChecked = []
            for currentlyChecked in range(len(xOccupied)):
                xConditionChecked.append(xWidthOccupied[currentlyChecked] <= object.x or object.x <= xOccupied[currentlyChecked])

            if object.y == self.floor1Y - object.height:
                for doorOnFloor in self.doorsPositions[self.floor1Y]:
                    doorsChecked.append((self.doorsPositions[self.floor1Y][doorOnFloor] + object.width + 5 <= object.x) or (object.x <= doorOnFloor - object.width - 5))
            elif object.y == self.floor2Y - object.height:
                for doorOnFloor in self.doorsPositions[self.floor2Y]:
                    doorsChecked.append((self.doorsPositions[self.floor2Y][doorOnFloor] + object.width + 5 <= object.x) or (object.x <= doorOnFloor - object.width - 5))
            elif object.y == self.floor3Y - object.height:
                for doorOnFloor in self.doorsPositions[self.floor3Y]:
                    doorsChecked.append((self.doorsPositions[self.floor3Y][doorOnFloor] + object.width + 5 <= object.x) or (object.x <= doorOnFloor - object.width - 5))

            while not all(xConditionChecked) and not all(doorsChecked):
                self.objectPositionSelect(object)
                xConditionChecked = []
                doorsChecked = []
                for currentlyChecked in range(len(xOccupied)):
                    xConditionChecked.append(xWidthOccupied[currentlyChecked] <= object.x or object.x <= xOccupied[currentlyChecked])
                if object.y == self.floor1Y - object.height:
                    for doorOnFloor in self.doorsPositions[self.floor1Y]:
                        doorsChecked.append((self.doorsPositions[self.floor1Y][doorOnFloor] + object.width + 5 <= object.x) or (object.x <= doorOnFloor - object.width - 5))
                elif object.y == self.floor2Y - object.height:
                    for doorOnFloor in self.doorsPositions[self.floor2Y]:
                        doorsChecked.append((self.doorsPositions[self.floor2Y][doorOnFloor] + object.width + 5 <= object.x) or (object.x <= doorOnFloor - object.width - 5))
                elif object.y == self.floor3Y - object.height:
                    for doorOnFloor in self.doorsPositions[self.floor3Y]:
                        doorsChecked.append((self.doorsPositions[self.floor3Y][doorOnFloor] + object.width + 5 <= object.x) or (object.x <= doorOnFloor - object.width - 5))         
