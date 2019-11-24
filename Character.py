import pygame
import random
import Equipment
import Interface

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

CHARACTER_HEIGHT = 64
CHARACTER_WIDTH = 64


class Player(pygame.Rect):
    walkLeft = [pygame.image.load("./resources/characters/hero/L1.png"), pygame.image.load("./resources/characters/hero/L2.png"), pygame.image.load("./resources/characters/hero/L3.png"),
                pygame.image.load("./resources/characters/hero/L4.png"), pygame.image.load("./resources/characters/hero/L5.png"), pygame.image.load("./resources/characters/hero/L6.png"),
                pygame.image.load("./resources/characters/hero/L7.png"), pygame.image.load("./resources/characters/hero/L8.png"), pygame.image.load("./resources/characters/hero/L9.png")]

    walkRight = [pygame.image.load("./resources/characters/hero/R1.png"), pygame.image.load("./resources/characters/hero/R2.png"), pygame.image.load("./resources/characters/hero/R3.png"),
                 pygame.image.load("./resources/characters/hero/R4.png"), pygame.image.load("./resources/characters/hero/R5.png"), pygame.image.load("./resources/characters/hero/R6.png"),
                 pygame.image.load("./resources/characters/hero/R7.png"), pygame.image.load("./resources/characters/hero/R8.png"), pygame.image.load("./resources/characters/hero/R9.png")]
    walkFloor = [pygame.image.load("./resources/characters/hero/D1.png"), pygame.image.load("./resources/characters/hero/D2.png"), pygame.image.load("./resources/characters/hero/D3.png")]

    stay = pygame.image.load("./resources/characters/hero/standing.png")

    def __init__(self, screen, building, screenX, screenY):
        self.screen = screen
        self.building = building
        pygame.Rect.__init__(self, (0, 0, CHARACTER_WIDTH, CHARACTER_HEIGHT))
        self.interface = Interface.Interface(screen, screenX, screenY)
        self.spawn()
        self.playerImage = self.stay
        self.speed = 5
        self.goingLeft = False
        self.goingRight = False
        self.regenTimer = 40
        self.regenCounter = 0
        self.regenCooldownCounter = 0
        self.regenCooldown = 10
        self.healthRegen = 2
        self.mentalityRegen = 1
        self.moving = False
        self.atDoor = False
        self.inDoor = False
        self.doorMoveCount = 0
        self.doorMoveTime = 20
        self.walkCount = 0
        self.setHealth(random.randint(30, 70))
        self.setMentality(30 + 70 - self.health)
        self.weapon = 0
        self.consumable = 0
        self.destinationEquipment = 0
        self.equipmentDestroyed = False
        self.destinationEnemy = 0
        self.enemyKilled = False
        self.experience = 0
        self.time = "22:00"
        if self.building.floor2Y <= self.y <= self.building.floorY:
            if self.building.leftWallX <= self.x <= self.building.floor1LeftColumnX - self.width:
                self.currentFloor = 0
            if self.building.floor1RightColumnX <= self.x <= self.building.rightWallX - self.width:
                self.currentFloor = 1
        elif self.building.floor3Y <= self.y <= self.building.floor2Y:
            self.currentFloor = 2
        elif self.building.ceilingY <= self.y <= self.building.floor3Y:
            self.currentFloor = 3
        self.destinationFloor = self.currentFloor
        self.onWayToFloor = self.currentFloor

    def spawn(self):
        self.building.spawnObject(self)

    def update(self):
        if not self.inDoor:
            self.control()
            self.regeneration()
            self.animation()
            if self.moving:
                self.moveToDestination()
            self.screen.blit(self.playerImage, self)
        else:
            self.doorMoveCount += 1
            if self.doorMoveCount == self.doorMoveTime:
                self.doorMoveCount = 0
                self.newFloorReached()
        self.interface.update()

    def animation(self):
        if self.goingLeft:
            self.regenCounter = 0
            self.playerImage = self.walkLeft[self.walkCount//3]
            self.walkCount += 1
        elif self.goingRight:
            self.regenCounter = 0
            self.playerImage = self.walkRight[self.walkCount // 3]
            self.walkCount += 1
            self.dead = True
        elif self.atDoor:
            self.regenCounter = 0
            self.playerImage = self.walkFloor[self.walkCount // 9]
            self.walkCount += 1
            if self.walkCount == 27:
                self.walkCount = 0
                self.atDoor = False
                self.inDoor = True
        else:
            self.playerImage = self.stay
            self.regenCounter += 1
        self.walkCount %= 27

    def control(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()

        if mouseClick[MOUSE_BUTTON_RIGHT] and self.building.leftWallX <= mouse[MOUSE_POS_X] <= self.building.rightWallX and self.building.ceilingY <= mouse[MOUSE_POS_Y] <= self.building.floorY:
            self.destinationEquipment = 0
            self.destinationEnemy = 0
            self.atDoor = False
            destinationFloor = mouse[MOUSE_POS_Y]
            destination = mouse[MOUSE_POS_X] - self.width // 2
            if not (self.building.floor2Y <= mouse[MOUSE_POS_Y] <= self.building.floorY
                    and self.building.floor1LeftColumnX <= mouse[MOUSE_POS_X] <= self.building.floor1RightColumnX):
                if self.building.floor2Y <= mouse[MOUSE_POS_Y] <= self.building.floorY:
                    if self.building.floor1RightColumnX <= mouse[MOUSE_POS_X] <= self.building.floor1RightColumnX + self.width // 2:
                        destination = self.building.floor1RightColumnX
                    elif self.building.floor1LeftColumnX - self.width <= mouse[MOUSE_POS_X] <= self.building.floor1LeftColumnX:
                        destination = self.building.floor1LeftColumnX - self.width
                if self.building.leftWallX <= mouse[MOUSE_POS_X] <= self.building.leftWallX + self.width // 2:
                    destination = self.building.leftWallX
                elif self.building.rightWallX - self.width <= mouse[MOUSE_POS_X] <= self.building.rightWallX:
                    destination = self.building.rightWallX - self.width
                self.setPath(destination, destinationFloor)

    def statusUpdate(self):
        if self.enemyKilled:
            self.enemyKilled = False
            return 1
        elif self.equipmentDestroyed:
            self.equipmentDestroyed = False
            return 2

    def moveToDestination(self):
        if self.destinationEquipment != 0:
            self.goForEquipment()
        if self.destinationEnemy != 0:
            self.fightMonster()

        if self.currentFloor == self.destinationFloor:
            if self.x < self.destination:
                if self.destination - self.x < self.speed:
                    self.move_ip((self.destination - self.x), 0)
                else:
                    self.move_ip(+self.speed, 0)
                self.goingLeft = False
                self.goingRight = True
            elif self.x > self.destination:
                if self.x - self.destination < self.speed:
                    self.move_ip((self.destination - self.x), 0)
                else:
                    self.move_ip(-self.speed, 0)
                self.goingLeft = True
                self.goingRight = False
            if self.x == self.destination:
                self.moving = False
                self.goingLeft = False
                self.goingRight = False
                self.walkCount = 0
        else:
            if self.currentFloor == 0 and self.onWayToFloor == 1:
                destinationDoor = self.building.stoneDoor1X
            elif self.currentFloor == 1 and self.onWayToFloor == 0:
                destinationDoor = self.building.stoneDoor2X
            elif self.currentFloor == 1 and self.onWayToFloor == 2:
                destinationDoor = self.building.woodenDoor1X
            elif self.currentFloor == 2 and self.onWayToFloor == 1:
                destinationDoor = self.building.woodenDoor2X
            elif self.currentFloor == 2 and self.onWayToFloor == 3:
                destinationDoor = self.building.oldDoor1X
            elif self.currentFloor == 3 and self.onWayToFloor == 2:
                destinationDoor = self.building.oldDoor2X

            if self.x < destinationDoor:
                if destinationDoor - self.x < self.speed:
                    self.move_ip((destinationDoor - self.x), 0)
                else:
                    self.move_ip(+self.speed, 0)
                self.goingLeft = False
                self.goingRight = True
            elif self.x > destinationDoor:
                if self.x - destinationDoor < self.speed:
                    self.move_ip((destinationDoor - self.x), 0)
                else:
                    self.move_ip(-self.speed, 0)
                self.goingLeft = True
                self.goingRight = False
            if self.x == destinationDoor:
                self.moving = False
                self.goingLeft = False
                self.goingRight = False
                self.walkCount = 0
                self.atDoor = True    

    def newFloorReached(self):
        lastFloor = self.currentFloor
        self.currentFloor = self.onWayToFloor
        if self.destinationFloor > self.currentFloor:
            self.onWayToFloor += 1
        elif self.destinationFloor < self.currentFloor:
            self.onWayToFloor -= 1
        else:
            self.onWayToFloor = self.destinationFloor
        self.inDoor = False
        if self.currentFloor == 0:
            self.x = self.building.stoneDoor1X
        if self.currentFloor == 1 and lastFloor == 0:
            self.x = self.building.stoneDoor2X
        if self.currentFloor == 1 and lastFloor == 2:
            self.x = self.building.woodenDoor1X
            self.y = self.building.floor1Y - self.height
        elif self.currentFloor == 2 and lastFloor == 1:
            self.x = self.building.woodenDoor2X
            self.y = self.building.floor2Y - self.height
        elif self.currentFloor == 2 and lastFloor == 3:
            self.x = self.building.oldDoor1X
            self.y = self.building.floor2Y - self.height
        elif self.currentFloor == 3:
            self.x = self.building.oldDoor2X
            self.y = self.building.floor3Y - self.height
        if not (self.x == self.destination):
            self.moving = True

    def setPath(self, destinationX, destinationY):
        self.destination = destinationX

        if self.building.floor2Y <= destinationY <= self.building.floorY:
            if self.building.leftWallX <= self.destination <= self.building.floor1LeftColumnX - self.width:
                self.destinationFloor = 0
            if self.building.floor1RightColumnX <= self.destination <= self.building.rightWallX - self.width:
                self.destinationFloor = 1
        elif self.building.floor3Y <= destinationY <= self.building.floor2Y:
            self.destinationFloor = 2
        elif self.building.ceilingY <= destinationY <= self.building.floor3Y:
            self.destinationFloor = 3
        if not (self.currentFloor == self.destinationFloor):
            if self.destinationFloor < self.currentFloor:
                self.onWayToFloor = self.currentFloor - 1
            elif self.destinationFloor > self.currentFloor:
                self.onWayToFloor = self.currentFloor + 1

        self.moving = True

    def teleport(self, x, y):
        self.x = x
        self.y = y
        self.setPath(self.x, self.y)
        self.currentFloor = self.destinationFloor

    def getPath(self):
        return self.destination

    def setHealth(self, newHealth):
        if newHealth > 100:
            newHealth = 100
        self.health = newHealth
        self.interface.health.setInformation(str(newHealth) + "/100")
        self.interface.healthBar.setValue(int(newHealth))

    def getHealth(self):
        return self.health

    def setMentality(self, newMentality):
        if newMentality > 100:
            newMentality = 100
        self.mentality = newMentality
        self.interface.mentality.setInformation(str(newMentality) + "/100")
        self.interface.mentalityBar.setValue(int(newMentality))

    def getMentality(self):
        return self.mentality

    def goForEquipment(self):
        if (type(self.destinationEquipment) == Equipment.Sword or type(self.destinationEquipment) == Equipment.Shield or type(self.destinationEquipment) == Equipment.Whip) \
                and abs((self.x + self.width // 2 ) - (self.destinationEquipment.x + self.destinationEquipment.width // 2)) <= 20 and abs(self.y - self.destinationEquipment.y) < 100:
            if self.weapon != 0:
                self.weapon.drop(self.destinationEquipment.x, self.destinationEquipment.y)
            self.setWeapon(self.destinationEquipment)
            self.destinationEquipment = 0
        if (type(self.destinationEquipment) == Equipment.Bomb or type(self.destinationEquipment) == Equipment.Garlic or type(self.destinationEquipment) == Equipment.Flute or
            type(self.destinationEquipment) == Equipment.Rune) and abs((self.x + self.width // 2) - (self.destinationEquipment.x + self.destinationEquipment.width // 2)) <= 20\
            and abs(self.y - self.destinationEquipment.y) < 100:
            if self.consumable != 0:
                self.consumable.drop(self.destinationEquipment.x, self.destinationEquipment.y)
            self.setConsumable(self.destinationEquipment)
            self.destinationEquipment = 0

    def fightMonster(self):
        if abs((self.x + self.width // 2) - (self.destinationEnemy.x + self.destinationEnemy.width // 2)) <= 20 and abs(self.y - self.destinationEnemy.y) < 100:
            self.setHealth(self.getHealth() - self.destinationEnemy.physicalPower)
            self.setMentality(self.getMentality() - self.destinationEnemy.mentalPower)
            self.setExperience(self.getExperience() + self.destinationEnemy.experienceReward)
            pygame.mixer.Sound("./resources/sound/fight.wav").play()
            self.destinationEnemy.dead = True
            self.enemyKilled = True
            self.destinationEnemy = 0

    def destroyWeapon(self):
        self.weapon.destroyed = True
        self.weapon = 0
        self.interface.equipment1.setInformation("Nothing")

    def destroyConsumable(self):
        self.consumable.destroyed = True
        self.consumable = 0
        self.interface.equipment2.setInformation("Nothing")

    def regeneration(self):
        if self.regenCounter > self.regenTimer:
            self.regenCooldownCounter += 1
            if self.regenCooldownCounter == self.regenCooldown:
                self.setHealth(self.getHealth() + self.healthRegen)
                self.setMentality(self.getMentality() + self.mentalityRegen)
                self.regenCooldownCounter = 0

    def setWeapon(self, newWeapon):
        self.weapon = newWeapon
        newWeapon.pickUp(self.interface.equipment1.x - Equipment.ICON_WIDTH - 3, self.interface.equipment1.y - 5)
        if self.weapon == 0:
            self.interface.equipment1.setInformation("Nothing")
        else:
            self.interface.equipment1.setInformation(self.weapon.getName())

    def getWeapon(self):
        return self.weapon

    def setConsumable(self, newConsumable):
        self.consumable = newConsumable
        newConsumable.pickUp(self.interface.equipment2.x - Equipment.ICON_WIDTH - 3, self.interface.equipment1.y - 5)
        if self.consumable == 0:
            self.interface.equipment2.setInformation("Nothing")
        else:
            self.interface.equipment2.setInformation(self.consumable.getName())

    def getConsumable(self):
        return self.consumable

    def setExperience(self, newExperience):
        self.experience = newExperience
        self.interface.score.setInformation(str(newExperience))

    def getExperience(self):
        return self.experience

    def setTime(self, newTime):
        self.time = newTime
        self.interface.time.setInformation(str(newTime))

    def getTime(self):
        return self.time

