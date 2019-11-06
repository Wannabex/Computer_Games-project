import pygame, random
import Character, Weather, Interface, Building, Sound, Trash, Equipment

class Game(object):
    def __init__(self, screen, screenSize):
        self.screen = screen
        self.screenSize = screenSize
        self.screenWidth, self.screenHeight = screenSize
        self.background = pygame.image.load("./resources/images/environment/background.png")
        self.background = pygame.transform.scale(self.background, screenSize)
        self.gameInit()
        self.exitGame = False

    def update(self):
        self.onRender()
        self.onLoop()

    def onLoop(self):
        self.hero.control()
        if self.hero.statusChanged:
            self.interface.updateStatus(self.hero.getExperience(), "22:01", self.hero.getWeapon(),
                                        self.hero.getConsumable(), self.hero.getHealth(), self.hero.getMentality())
            self.hero.statusChanged = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.hero.setExperience(random.randint(10, 24214))
            self.sky.monster.itsTime = True
            self.sounds.monsterRoar()
        if keys[pygame.K_DOWN]:
            self.hero.setHealth(random.randint(1, 100))
            self.sky.thunder.itsTime = True
            self.sounds.thunderstorm()
        if keys[pygame.K_RIGHT]:
            self.exitGame = True
            self.sounds.stopSounds()
            del self

    def onRender(self):
        self.screen.blit(self.background, [0, 0])
        self.sky.update()
        for column in self.weather:
            column.update()
        # self.building.update()
        self.interface.update()
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
        self.interface = Interface.Interface(self.screen, self.screenWidth, self.screenHeight)
        self.hero = Character.Player(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Character.CHARACTER_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Character.CHARACTER_HEIGHT - 3))
        self.hero.setConstraints(self.building.getWalls())

        self.cultist = Trash.Cultist(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Trash.Cultist.CULTIST_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Trash.Cultist.CULTIST_HEIGHT - 3))
        self.angel = Trash.Angel(self.screen,
                                 random.randint(self.building.leftWallX,
                                                self.building.rightWallX - Trash.Angel.ANGEL_WIDTH),
                                 random.randint(self.building.ceilingY,
                                                self.building.floorY - Trash.Angel.ANGEL_HEIGHT - 3))
        self.skeleton = Trash.Skeleton(self.screen,
                                       random.randint(self.building.leftWallX,
                                                      self.building.rightWallX - Trash.Skeleton.SKELETON_WIDTH),
                                       random.randint(self.building.ceilingY,
                                                      self.building.floorY - Trash.Skeleton.SKELETON_HEIGHT - 3))
        self.bomb = Equipment.Bomb(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.garlic = Equipment.Garlic(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.flute = Equipment.Flute(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.rune = Equipment.Rune(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.sword = Equipment.Sword(self.screen,
                                     random.randint(self.building.leftWallX,
                                                    self.building.rightWallX - Equipment.ICON_WIDTH),
                                     random.randint(self.building.ceilingY,
                                                    self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.whip = Equipment.Whip(self.screen,
                                   random.randint(self.building.leftWallX,
                                                  self.building.rightWallX - Equipment.ICON_WIDTH),
                                   random.randint(self.building.ceilingY,
                                                  self.building.floorY - Equipment.ICON_WIDTH - 3))
        self.shield = Equipment.Shield(self.screen,
                                       random.randint(self.building.leftWallX,
                                                      self.building.rightWallX - Equipment.ICON_WIDTH),
                                       random.randint(self.building.ceilingY,
                                                      self.building.floorY - Equipment.ICON_WIDTH - 3))


