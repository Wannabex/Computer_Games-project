import pygame, random
import Character, Rain, Interface


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
        self.houseLeftWallX = 100
        self.houseRightWallX = 850
        self.houseRoofY = 100
        self.houseFloorY = self.screenHeight - 74
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
        self.sounds_init()
        self.clock.tick(27)
        self._running = True
        for columnNumber in range (1, self.houseLeftWallX // Rain.SIZE):
            self.weather.append(Rain.Column(columnNumber * Rain.SIZE, self._display_surf, self.screenHeight))
        for columnNumber in range(self.houseLeftWallX // Rain.SIZE, self.houseRightWallX // Rain.SIZE):
            self.weather.append(Rain.Column(columnNumber * Rain.SIZE, self._display_surf, self.houseRoofY))
        for columnNumber in range (self.houseRightWallX // Rain.SIZE, self.screenWidth // Rain.SIZE):
            self.weather.append(Rain.Column(columnNumber * Rain.SIZE, self._display_surf, self.screenHeight))
        self.interface = Interface.Interface(self._display_surf, self.screenWidth, self.screenHeight)
        self.hero = Character.Player(random.randint(self.houseLeftWallX, self.houseRightWallX),
                                     random.randint(self.houseRoofY, self.houseFloorY))

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.hero.y > self.houseRoofY:
            self.hero.move_ip(0, -self.hero.characterSpeed)
            self.hero.goingLeft = False
            self.hero.goingRight = False
            self.thunderstorm()
        if keys[pygame.K_DOWN] and self.hero.y < self.houseFloorY:
            self.hero.move_ip(0, +self.hero.characterSpeed)
            self.hero.goingLeft = False
            self.hero.goingRight = False
        if keys[pygame.K_LEFT] and self.hero.x > self.houseLeftWallX:
            self.hero.move_ip(-self.hero.characterSpeed, 0)
            self.hero.goingLeft = True
            self.hero.goingRight = False
        elif keys[pygame.K_RIGHT] and self.hero.x < self.houseRightWallX - self.hero.width:
            self.hero.move_ip(+self.hero.characterSpeed, 0)
            self.hero.goingLeft = False
            self.hero.goingRight = True
        else:
            self.hero.goingLeft = False
            self.hero.goingRight = False
            self.hero.walkCount = 0

    def on_render(self):
        self._display_surf.blit(self.background, [0, 0])
        for column in self.weather:
            column.update()
        self.interface.update()
        self.hero.animation()
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