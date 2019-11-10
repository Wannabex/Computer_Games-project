import pygame, random
import Character, Weather, Building, Sound, Trash, Equipment, Interface


class Game(object):
    def __init__(self, screen, screenSize):
        self.screen = screen
        self.screenSize = screenSize
        self.screenWidth, self.screenHeight = screenSize
        self.background = pygame.image.load("./resources/images/environment/background.png")
        self.background = pygame.transform.scale(self.background, screenSize)
        self.gameInit()
        self.actionWheel = 0
        self.exitGame = False

    def update(self):
        self.onLoop()
        self.onRender()

    def onLoop(self):
        if not self.actionWheel:
            for enemy in self.enemies:
                if enemy.actionsVisible:
                    self.actionWheel = Interface.ActionWheel(self.screen, enemy, weapon=self.checkCurrentWeapon(self.items), consumable=self.checkCurrentConsumable(self.items), takeable=False)
                    self.objectWithInterface = enemy
                    self.changeClickable(self.items, self.enemies, self.objectWithInterface, newState=False)
            for item in self.items:
                if item.actionsVisible:
                    self.actionWheel = Interface.ActionWheel(self.screen, item)
                    self.objectWithInterface = item
                    self.changeClickable(self.items, self.enemies, self.objectWithInterface, newState=False)
        else:
            if self.objectWithInterface.wheelEvents(self.actionWheel.wheelEvents()) == 1:
                del self.actionWheel
                self.actionWheel = 0
                self.changeClickable(self.items, self.enemies)


        self.hero.control()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.hero.setExperience(random.randint(10, 24214))
            self.sky.monster.itsTime = True
            self.sounds.monsterRoar()
            self.hero.setConsumable(self.bomb)
        if keys[pygame.K_DOWN]:
            self.hero.setHealth(random.randint(1, 100))
            self.sky.thunder.itsTime = True
            self.sounds.thunderstorm()
            self.hero.setWeapon(self.sword)
        if keys[pygame.K_RIGHT]:
            self.exitGame = True
            self.sounds.stopSounds()
            del self

    def onRender(self):
        self.screen.blit(self.background, [0, 0])
        self.sky.update()
        #for column in self.weather:
        #    column.update()
        # self.building.update()
        self.cultist.update()
        self.angel.update()
        self.skeleton.update()
        self.whip.update()
        self.shield.update()
        self.sword.update()
        self.bomb.update()
        self.garlic.update()
        self.flute.update()
        self.rune.update()
        if self.actionWheel != 0:
            self.actionWheel.update()
        self.hero.update()
        self.screen.blit(self.hero.playerImage, self.hero)


    def gameInit(self):
        self.sounds = Sound.Sound()
        self.building = Building.Building(self.screen, self.screenSize)
        self.weather = []
        for columnNumber in range(1, self.building.leftWallX // Weather.SIZE):
            self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self.screen, self.building.floorY))
        for columnNumber in range(self.building.leftWallX // Weather.SIZE, self.building.rightWallX // Weather.SIZE):
            self.weather.append(
                Weather.Column(columnNumber * Weather.SIZE, self.screen, self.building.leftWallX))
        for columnNumber in range(self.building.rightWallX // Weather.SIZE, self.screenWidth // Weather.SIZE):
            self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self.screen, self.building.floorY))
        self.sky = Weather.Sky(self.screen, self.screenWidth, self.screenHeight, self.building.leftWallX,
                               self.building.rightWallX, self.building.ceilingY)
        self.hero = Character.Player(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Character.CHARACTER_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Character.CHARACTER_HEIGHT - 3),
                                     self.screenWidth, self.screenHeight)
        self.hero.setConstraints(self.building.getWalls())

        self.enemies = []
        self.items = []
        self.cultist = Trash.Cultist(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Trash.Cultist.CULTIST_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Trash.Cultist.CULTIST_HEIGHT - 3))
        self.enemies.append(self.cultist)
        self.angel = Trash.Angel(self.screen,
                                 random.randint(self.building.leftWallX,
                                                self.building.rightWallX - Trash.Angel.ANGEL_WIDTH),
                                 random.randint(self.building.ceilingY,
                                                self.building.floorY - Trash.Angel.ANGEL_HEIGHT - 3))
        self.enemies.append(self.angel)
        self.skeleton = Trash.Skeleton(self.screen,
                                       random.randint(self.building.leftWallX,
                                                      self.building.rightWallX - Trash.Skeleton.SKELETON_WIDTH),
                                       random.randint(self.building.ceilingY,
                                                      self.building.floorY - Trash.Skeleton.SKELETON_HEIGHT - 3))
        self.enemies.append(self.skeleton)
        self.bomb = Equipment.Bomb(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.bomb)
        self.garlic = Equipment.Garlic(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.garlic)
        self.flute = Equipment.Flute(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.flute)
        self.rune = Equipment.Rune(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.rune)
        self.sword = Equipment.Sword(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.sword)
        self.whip = Equipment.Whip(self.screen,
                                   random.randint(self.building.leftWallX,
                                                  self.building.rightWallX - Equipment.ICON_WIDTH),
                                   random.randint(self.building.ceilingY,
                                                  self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.whip)
        self.shield = Equipment.Shield(self.screen,
                                       random.randint(self.building.leftWallX,
                                                      self.building.rightWallX - Equipment.ICON_WIDTH),
                                       random.randint(self.building.ceilingY,
                                                      self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.items.append(self.shield)

    def checkFreePositions(self):
        pass

    def checkCurrentWeapon(self, items):
        if self.hero.weapon != "Nothing":
            for item in items:
                if item.name == self.hero.weapon:
                    return item.wheelIcon
        else:
            return 0

    def checkCurrentConsumable(self, items):
        if self.hero.consumable != "Nothing":
            for item in items:
                if item.name == self.hero.consumable:
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

