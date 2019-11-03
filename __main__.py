import pygame, random
import Character, Weather, Interface, Building, Sound


class App:
    def __init__(self):
        pygame.init()
        self._running = True
        self._display_surf = None
        self.clock = pygame.time.Clock()
        self.screenInfo = pygame.display.Info()
        self.screenSize = self.screenWidth, self.screenHeight = self.screenInfo.current_w - 400, self.screenInfo.current_h - 250
        self.background = pygame.image.load("./resources/images/background.png")
        self.background = pygame.transform.scale(self.background, self.screenSize)
        self.thunderSounds = []
        self.thunderCounter = 0
        self.weather = []

    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF )# | pygame.FULLSCREEN)
        pygame.display.set_caption("Trashing and Rushing")
        self.building = Building.Building(self._display_surf, self.screenSize)
        for columnNumber in range (1, self.building.leftWallX // Weather.SIZE):
            self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self._display_surf, self.building.floorY))
        for columnNumber in range(self.building.leftWallX // Weather.SIZE, self.building.rightWallX // Weather.SIZE):
            self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self._display_surf, self.building.leftWallX))
        for columnNumber in range (self.building.rightWallX // Weather.SIZE, self.screenWidth // Weather.SIZE):
            self.weather.append(Weather.Column(columnNumber * Weather.SIZE, self._display_surf, self.building.floorY))
        self.sky = Weather.Sky(self._display_surf, self.screenWidth, self.screenHeight, self.building.leftWallX, self.building.rightWallX, self.building.ceilingY)
        self.interface = Interface.Interface(self._display_surf, self.screenWidth, self.screenHeight)
        self.hero = Character.Player(self._display_surf, random.randint(self.building.leftWallX, self.building.rightWallX),
                                     random.randint(self.building.ceilingY, self.building.floorY - Character.CHARACTER_HEIGHT - 3))
        self.hero.setConstraints(self.building.getWalls())
        self.sounds = Sound.Sound()
        self.clock.tick(27)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
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

    def on_render(self):
        self._display_surf.blit(self.background, [0, 0])
        self.sky.update()
        for column in self.weather:
            column.update()
        #self.building.update()
        self.interface.update()
        self.hero.update()
        self._display_surf.blit(self.hero.playerImage, self.hero)
        pygame.display.update()

    def on_cleanup(self):
        pass

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()