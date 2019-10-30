import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        pygame.init()
        self.ScreenInfo = pygame.display.Info()
        self.screenSize = self.screenWidth, self.screenHeight = self.ScreenInfo.current_w - 400, self.ScreenInfo.current_h - 200
        self.characterX, self.characterY, self.characterWidth, self.characterHeight = 50, 50, 40, 60
        self.characterSpeed = 2
        self.thunderSounds = []
        self.thunderCounter = 0

    def sounds_init(self):
        pygame.mixer.music.load("./resources/sound/music.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        rainSound = pygame.mixer.Sound("./resources/sound/rain_ambience.wav")
        rainSound.set_volume(0.8)
        rainSound.play(-1)

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
        self._display_surf = pygame.display.set_mode(self.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF )  #| pygame.FULLSCREEN)
        self.sounds_init()
        pygame.display.set_caption("Trashing and Rushing")
        pygame.time.delay(100)



        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.characterX > 0:
            self.characterX -= self.characterSpeed

        if keys[pygame.K_RIGHT] and self.characterX < self.screenWidth - self.characterWidth:
            self.characterX += self.characterSpeed

        if keys[pygame.K_UP] and self.characterY > 0:
            self.characterY -= self.characterSpeed
            self.thunderstorm()

        if keys[pygame.K_DOWN] and self.characterY < self.screenHeight - self.characterHeight:
            self.characterY += self.characterSpeed

        characterRect = self.characterX, self.characterY, self.characterWidth, self.characterHeight
        pygame.draw.rect(self._display_surf, (255, 0, 0), characterRect)
        pygame.display.update()

    def on_render(self):
        pass

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