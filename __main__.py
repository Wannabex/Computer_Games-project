import pygame
import Character

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        pygame.init()

        self. clock = pygame.time.Clock()
        self.ScreenInfo = pygame.display.Info()
        self.screenSize = self.screenWidth, self.screenHeight = self.ScreenInfo.current_w - 500, self.ScreenInfo.current_h - 250
        self.hero = Character.Player()

        self.thunderSounds = []
        self.thunderCounter = 0
        self.background = pygame.image.load("./resources/images/background.png")
        self.background = pygame.transform.scale(self.background, self.screenSize)


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
        #self.sounds_init()
        self.clock.tick(27)
        self._running = True


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.hero.x > 0:
            self.hero.move_ip(-self.hero.characterSpeed, 0)
            self.hero.goingLeft = True
            self.hero.goingRight = False
        if keys[pygame.K_RIGHT] and self.hero.x < self.screenWidth - self.hero.width:
            self.hero.move_ip(+self.hero.characterSpeed, 0)
            self.hero.goingLeft = False
            self.hero.goingRight = True
        if keys[pygame.K_UP] and self.hero.y > 0:
            self.hero.move_ip(0, -self.hero.characterSpeed)
            self.hero.goingLeft = False
            self.hero.goingRight = False
            #self.thunderstorm()
        if keys[pygame.K_DOWN] and self.hero.y < self.screenHeight - self.hero.height:
            self.hero.move_ip(0, +self.hero.characterSpeed)
            self.hero.positionY += self.hero.characterSpeed
            self.hero.goingLeft = False
            self.hero.goingRight = False
        self.hero.animation()


    def on_render(self):
        self._display_surf.blit(self.background, [0, 0])
        self._display_surf.blit(self.hero.playerImage, self.hero.position)
        #pygame.draw.rect(self._display_surf, (255, 0, 0), self.hero)
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