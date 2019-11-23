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
        self.objectsPositions = {self.floor1Y: {},
                                 self.floor2Y: {},
                                 self.floor3Y: {}}
        print(len(self.objectsPositions))
        print(len(self.objectsPositions[self.floor1Y]))
        print(len(self.objectsPositions[self.floor2Y]))
        print(len(self.objectsPositions[self.floor3Y]))
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
        if object.y == self.floor1Y - object.height:
            self.objectsPositions[self.floor1Y].update({object.x: object.width})
        elif object.y == self.floor2Y - object.height:
            self.objectsPositions[self.floor2Y].update({object.x: object.width})
        elif object.y == self.floor3Y - object.height:
            self.objectsPositions[self.floor3Y].update({object.x: object.width})

    def objectPositionSelect(self, object):
        if type(object) == Trash.Angel:
            object.y = random.choice(self.floorsYs[0:2]) - object.height
        else:
            object.y = random.choice(self.floorsYs) - object.height
        if not (object.y == self.floor1Y - object.height):
            object.x = random.randint(self.leftWallX, self.rightWallX - object.width)
        else:
            side = random.randint(1, 2)
            if side == 1:
                object.x = random.randint(self.leftWallX, self.floor1LeftColumnX - object.width)
            else:
                object.x = random.randint(self.floor1RightColumnX, self.rightWallX - object.width)

    def checkFreePositions(self, object):
        positionsChecked = []
        doorsChecked = []
        spawnConditions = []

        if object.y == self.floor1Y - object.height:
            for doorOnFloor in self.doorsPositions[self.floor1Y]:
                doorsChecked.append((doorOnFloor + self.doorsPositions[self.floor1Y][doorOnFloor] + object.width <= object.x) or (object.x <= doorOnFloor - object.width))
            if len(self.currentlySpawned) > 1 and len(self.objectsPositions[self.floor1Y]) > 0:
                for objectOnFloor in self.objectsPositions[self.floor1Y]:
                    positionsChecked.append((objectOnFloor + self.objectsPositions[self.floor1Y][objectOnFloor] <= object.x) or (object.x <= objectOnFloor - object.width))
        elif object.y == self.floor2Y - object.height:
            for doorOnFloor in self.doorsPositions[self.floor2Y]:
                doorsChecked.append((doorOnFloor + self.doorsPositions[self.floor2Y][doorOnFloor] + object.width <= object.x) or (object.x <= doorOnFloor - object.width))
            if len(self.currentlySpawned) > 1 and len(self.objectsPositions[self.floor2Y]) > 0:
                for objectOnFloor in self.objectsPositions[self.floor2Y]:
                    positionsChecked.append((objectOnFloor + self.objectsPositions[self.floor2Y][objectOnFloor] <= object.x) or (object.x <= objectOnFloor - object.width))
        elif object.y == self.floor3Y - object.height:
            for doorOnFloor in self.doorsPositions[self.floor3Y]:
                doorsChecked.append((doorOnFloor + self.doorsPositions[self.floor3Y][doorOnFloor] + object.width <= object.x) or (object.x <= doorOnFloor - object.width))
            if len(self.currentlySpawned) > 1 and len(self.objectsPositions[self.floor3Y]) > 0:
                for objectOnFloor in self.objectsPositions[self.floor3Y]:
                    positionsChecked.append((objectOnFloor + self.objectsPositions[self.floor3Y][objectOnFloor] <= object.x) or (object.x <= objectOnFloor - object.width))
        if len(self.currentlySpawned) > 1:
            spawnConditions.extend(positionsChecked)
        spawnConditions.extend(doorsChecked)

        while not all(spawnConditions):
            self.objectPositionSelect(object)
            positionsChecked = []
            doorsChecked = []
            spawnConditions = []
            if object.y == self.floor1Y - object.height:
                for doorOnFloor in self.doorsPositions[self.floor1Y]:
                    doorsChecked.append((doorOnFloor + self.doorsPositions[self.floor1Y][doorOnFloor] + object.width <= object.x) or (object.x <= doorOnFloor - object.width))
                if len(self.currentlySpawned) > 1 and len(self.objectsPositions[self.floor1Y]) > 0:
                    for objectOnFloor in self.objectsPositions[self.floor1Y]:
                        positionsChecked.append((objectOnFloor + self.objectsPositions[self.floor1Y][objectOnFloor] <= object.x) or (object.x <= objectOnFloor - object.width))
            elif object.y == self.floor2Y - object.height:
                for doorOnFloor in self.doorsPositions[self.floor2Y]:
                    doorsChecked.append((doorOnFloor + self.doorsPositions[self.floor2Y][doorOnFloor] + object.width <= object.x) or (object.x <= doorOnFloor - object.width))
                if len(self.currentlySpawned) > 1 and len(self.objectsPositions[self.floor2Y]) > 0:
                    for objectOnFloor in self.objectsPositions[self.floor2Y]:
                        positionsChecked.append((objectOnFloor + self.objectsPositions[self.floor2Y][objectOnFloor] <= object.x) or (object.x <= objectOnFloor - object.width))
            elif object.y == self.floor3Y - object.height:
                for doorOnFloor in self.doorsPositions[self.floor3Y]:
                    doorsChecked.append((doorOnFloor + self.doorsPositions[self.floor3Y][doorOnFloor] + object.width <= object.x) or (object.x <= doorOnFloor - object.width))
                if len(self.currentlySpawned) > 1 and len(self.objectsPositions[self.floor3Y]) > 0:
                    for objectOnFloor in self.objectsPositions[self.floor3Y]:
                        positionsChecked.append((objectOnFloor + self.objectsPositions[self.floor3Y][objectOnFloor] <= object.x) or (object.x <= objectOnFloor - object.width))
            if len(self.currentlySpawned) > 1:
                spawnConditions.extend(positionsChecked)
            spawnConditions.extend(doorsChecked)