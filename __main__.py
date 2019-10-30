import pygame


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        pygame.init()
        self.ScreenInfo = pygame.display.Info()
        self.screenSize = self.screenWidth, self.screenHeight = self.ScreenInfo.current_w - 400, self.ScreenInfo.current_h - 200
        self.characterX, self.characterY, self.characterWidth, self.characterHeight = 50, 50, 40, 60
        self.characterSpeed = 5

    def on_init(self):
        self._display_surf = pygame.display.set_mode(self.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF )  #| pygame.FULLSCREEN)
        pygame.display.set_caption("Trashing and Rushing")
        pygame.time.delay(100)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.characterX -= self.characterSpeed
            if self.characterX < 0:
                self.characterX = 0
        if keys[pygame.K_RIGHT]:
            self.characterX += self.characterSpeed
            if self.characterX > self.screenWidth - self.characterWidth:
                self.characterX = self.screenWidth - self.characterWidth
        if keys[pygame.K_UP]:
            self.characterY -= self.characterSpeed
            if self.characterY < 0:
                self.characterY = 0
        if keys[pygame.K_DOWN]:
            self.characterY += self.characterSpeed
            if self.characterY > self.screenHeight - self.characterHeight:
                self.characterY = self.screenHeight - self.characterHeight

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