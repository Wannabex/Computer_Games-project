import pygame, random
import Character, Weather, Building, Sound, Trash, Equipment, Interface

class Game(object):
    def __init__(self, screen, screenSize):
        self.screen = screen
        self.screenSize = screenSize
        self.screenWidth, self.screenHeight = screenSize
        self.background = pygame.image.load("./resources/images/environment/background.png")
        self.background = pygame.transform.scale(self.background, screenSize)
        self.actionWheel = 0
        self.gameOver = False
        self.exitGame = False
        self.configFile = open("./resources/config.txt", 'r')
        self.fileContent = self.configFile.readline()
        if self.fileContent.endswith("True"):
            self.rainEffect = True
        elif self.fileContent.endswith("False"):
            self.rainEffect = False
        self.configFile.close()
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 80)
        self.overInformation = self.font.render("    GAME   OVER      ", True, (128, 0, 0))
        self.victoryInformation = self.font.render("  YOU SURVIVED      ", True, (0, 102, 0))
        rectWidth = 500
        rectHeight = 100
        self.overRect = pygame.Rect(( self.screenWidth // 4, self.screenHeight // 3, rectWidth, rectHeight))
        self.loadingMenuCounter = 7
        self.enemies = []
        self.equipment = []
        self.enemiesToSpawn = []
        self.equipmentToSpawn = []
        self.enemySpawnTime = random.randint(100, 150)
        self.equipmentSpawnTime = random.randint(20, 50)
        self.enemySpawnCounter = 0
        self.equipmentSpawnCounter = 0
        self.enemiesPresent = 0
        self.equipmentPresent = 0
        self.victorious = False

        self.gameInit()

    def update(self):
        if not self.gameOver:
            self.onLoop()
            self.onRender()
        else:
            self.sounds.stopSounds()
            mouseClick = pygame.mouse.get_pressed()
            if mouseClick[Interface.MOUSE_BUTTON_LEFT] or mouseClick[Interface.MOUSE_BUTTON_RIGHT]:
                self.loadingMenuCounter -= 1
                if self.loadingMenuCounter <= 0:
                    self.gameOver = False
                    self.exitGame = True
            self.screen.fill((0, 0, 0))
            if self.victorious:
                self.screen.blit(self.victoryInformation, self.overRect)
            else:
                self.screen.blit(self.overInformation, self.overRect)

    def onLoop(self):
        self.checkActionWheel()
        self.randomEnemySpawn()
        self.randomEquipmentSpawn()
        self.checkChanges()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.exitGame = True
            self.sounds.stopSounds()
            del self
        elif keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_RIGHT]:
            self.gameOver = True

    def onRender(self):
        self.screen .blit(self.background, [0, 0])
        self.sky.update()
        if self.rainEffect:
            for column in self.weather:
                column.update()
        self.building.update()

        for equipment in self.equipment:
            equipment.update()
        for enemy in self.enemies:
            enemy.update()
        if self.actionWheel != 0:
            self.actionWheel.update()
        self.hero.update()
        if self.hero.getHealth() <= 0 or self.hero.getMentality() <= 0:
            self.gameOver = True
        self.screen.blit(self.hero.playerImage, self.hero)

    def checkChanges(self):
        statusChange = self.hero.statusUpdate()
        if statusChange == 1:
            self.enemiesPresent -= 1
            cultist = Trash.Cultist(self.screen, self.building)
            self.enemiesToSpawn.append(cultist)
            skeleton = Trash.Cultist(self.screen, self.building)
            self.enemiesToSpawn.append(skeleton)
            self.enemySpawnCounter = 0
        elif statusChange == 2:
            self.equipmentPresent -= 1
            self.equipmentSpawnCounter = 0
        elif statusChange == 3:
            self.gameOver = True
            self.victorious = True

    def gameInit(self):
        self.sounds = Sound.Sound()
        self.building = Building.Building(self.screen, self.screenSize)
        if self.rainEffect:
            self.weather = []
            for columnNumber in range(1, self.building.leftWallX // Weather.SIZE):
                self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self.screen, self.building.floorY))
            for columnNumber in range(self.building.leftWallX // Weather.SIZE, self.building.rightWallX // Weather.SIZE):
                self.weather.append(
                    Weather.Column(columnNumber * Weather.SIZE, self.screen, self.building.leftWallX))
            for columnNumber in range(self.building.rightWallX // Weather.SIZE, self.screenWidth // Weather.SIZE):
                self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self.screen, self.building.floorY))
        self.sky = Weather.Sky(self.screen, self.screenWidth, self.screenHeight, self.building.leftWallX,
                               self.building.rightWallX, self.building.ceilingY, self.sounds)

        # RANDOMLY SPAWNED
        self.hero = Character.Player(self.screen, self.building, self.screenWidth, self.screenHeight)

        self.cultist = Trash.Cultist(self.screen, self.building)
        self.enemiesToSpawn.append(self.cultist)
        self.cultist2 = Trash.Cultist(self.screen, self.building)
        self.enemiesToSpawn.append(self.cultist2)

        self.angel = Trash.Angel(self.screen, self.building)
        #self.enemies.append(self.angel)
        #self.angel.spawn()
        self.enemiesToSpawn.append(self.angel)

        self.skeleton = Trash.Skeleton(self.screen, self.building)
        self.enemiesToSpawn.append(self.skeleton)
        self.skeleton2 = Trash.Skeleton(self.screen, self.building)
        self.enemiesToSpawn.append(self.skeleton2)

        self.bomb = Equipment.Bomb(self.screen, self.building)
        self.equipmentToSpawn.append(self.bomb)
        self.bomb2 = Equipment.Bomb(self.screen, self.building)
        self.equipmentToSpawn.append(self.bomb2)
        self.garlic = Equipment.Garlic(self.screen, self.building)
        self.equipmentToSpawn.append(self.garlic)
        self.garlic2 = Equipment.Garlic(self.screen, self.building)
        self.equipmentToSpawn.append(self.garlic2)
        self.flute = Equipment.Flute(self.screen, self.building)
        self.equipmentToSpawn.append(self.flute)
        self.flute2 = Equipment.Flute(self.screen, self.building)
        self.equipmentToSpawn.append(self.flute2)
        self.rune = Equipment.Rune(self.screen, self.building)
        self.equipmentToSpawn.append(self.rune)
        self.rune2 = Equipment.Rune(self.screen, self.building)
        self.equipmentToSpawn.append(self.rune2)
        self.rune3 = Equipment.Rune(self.screen, self.building)
        self.equipmentToSpawn.append(self.rune3)
        self.sword = Equipment.Sword(self.screen, self.building)
        self.equipmentToSpawn.append(self.sword)
        self.whip = Equipment.Whip(self.screen, self.building)
        self.equipmentToSpawn.append(self.whip)
        self.shield = Equipment.Shield(self.screen, self.building)
        self.equipmentToSpawn.append(self.shield)

    def randomEnemySpawn(self):
        self.enemySpawnCounter += 1
        if self.enemiesPresent < 4 and self.enemySpawnCounter >= self.enemySpawnTime:
            enemySpawning = random.choice(self.enemiesToSpawn)
            self.enemies.append(enemySpawning)
            enemySpawning.spawn()
            self.enemiesToSpawn.remove(enemySpawning)
            self.enemySpawnTime = random.randint(80, 250)
            self.enemySpawnCounter = 0
            self.enemiesPresent += 1
                        
    def randomEquipmentSpawn(self):
        self.equipmentSpawnCounter += 1
        if self.equipmentPresent < 9 and self.equipmentSpawnCounter >= self.equipmentSpawnTime:
            equipmentSpawning = random.choice(self.equipmentToSpawn)
            if self.equipmentPresent >= 2 and (not self.weaponAlreadySpawned()):
                while not (type(equipmentSpawning) == Equipment.Sword or type(equipmentSpawning) == Equipment.Shield or type(equipmentSpawning) == Equipment.Whip):
                    equipmentSpawning = random.choice(self.equipmentToSpawn)
            equipmentSpawning.spawn()
            self.equipment.append(equipmentSpawning)
            self.equipmentToSpawn.remove(equipmentSpawning)
            self.equipmentSpawnTime = random.randint(80, 160)
            self.equipmentSpawnCounter = 0
            self.equipmentPresent += 1            

    def weaponAlreadySpawned(self):
        for item in self.equipment:
            if type(item) == Equipment.Sword or type(item) == Equipment.Shield or type(item) == Equipment.Whip:
                return True
        return False

    def checkActionWheel(self):
        if not self.actionWheel:
            for enemy in self.enemies:
                if enemy.actionsVisible:
                    self.actionWheel = Interface.ActionWheel(self.screen, self.hero, enemy, weapon=self.checkCurrentWeapon(self.equipment), consumable=self.checkCurrentConsumable(self.equipment), takeable=False)
                    self.objectWithInterface = enemy
                    self.changeClickable(self.equipment, self.enemies, objectWithWheel=self.objectWithInterface, newState=False)
            for item in self.equipment:
                if item.actionsVisible:
                    self.actionWheel = Interface.ActionWheel(self.screen, self.hero, item)
                    self.objectWithInterface = item
                    self.changeClickable(self.equipment, self.enemies, objectWithWheel=self.objectWithInterface, newState=False)
        else:
            if self.objectWithInterface.wheelEvents(self.actionWheel.wheelEvents()) == 1:
                del self.actionWheel
                self.actionWheel = 0
                self.changeClickable(self.equipment, self.enemies)

    def checkCurrentWeapon(self, items):
        if self.hero.weapon != 0:
            for item in items:
                if item == self.hero.weapon:
                    return item.wheelIcon
        else:
            return 0

    def checkCurrentConsumable(self, items):
        if self.hero.consumable != 0:
            for item in items:
                if item == self.hero.consumable:
                    return item.wheelIcon
        else:
            return 0

    def changeClickable(self, items, enemies, objectWithWheel=0, newState=True):
        for item in items:
            if item != objectWithWheel:
                item.clickable = newState
        for enemy in enemies:
            if enemy != objectWithWheel:
                enemy.clickable = newState


