import pygame, random
import Character, Rain, Interface, Building


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

    def sounds_init(self):
        pygame.mixer.music.load("./resources/sound/music.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        ambience = pygame.mixer.Sound("./resources/sound/rain_ambience.wav")
        ambience.set_volume(0.8)
        ambience.play(-1)

        thunder1 = pygame.mixer.Sound("./resources/sound/thunder1.wav")
        thunder2 = pygame.mixer.Sound("./resources/sound/thunder2.wav")
        thunder3 = pygame.mixer.Sound("./resources/sound/thunder3.wav")
        self.thunderSounds.append(thunder1)
        self.thunderSounds.append(thunder2)
        self.thunderSounds.append(thunder3)

    def thunderstorm(self):
        self.thunderSounds[self.thunderCounter].play()
        self.thunderCounter += 1
        self.thunderCounter ^= 3

    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF )# | pygame.FULLSCREEN)
        pygame.display.set_caption("Trashing and Rushing")
        self.building = Building.Building(self._display_surf, self.screenSize)

        for columnNumber in range (1, self.building.leftWallX // Rain.SIZE):
            self.weather.append(Rain.Column(columnNumber * Rain.SIZE, self._display_surf, self.building.floorY))
        for columnNumber in range(self.building.leftWallX // Rain.SIZE, self.building.rightWallX // Rain.SIZE):
            self.weather.append(Rain.Column(columnNumber * Rain.SIZE, self._display_surf, self.building.leftWallX))
        for columnNumber in range (self.building.rightWallX // Rain.SIZE, self.screenWidth // Rain.SIZE):
            self.weather.append(Rain.Column(columnNumber * Rain.SIZE, self._display_surf, self.building.floorY))
        self.interface = Interface.Interface(self._display_surf, self.screenWidth, self.screenHeight)
        self.hero = Character.Player(self._display_surf, random.randint(self.building.leftWallX, self.building.rightWallX),
                                     random.randint(self.building.ceilingY, self.building.floorY))
        self.hero.setConstraints(self.building.getWalls())
        self.sounds_init()
        self.clock.tick(27)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.hero.control()

    def on_render(self):
        self._display_surf.blit(self.background, [0, 0])
        for column in self.weather:
            column.update()
        self.interface.update()
        self.hero.animation()
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