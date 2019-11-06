import pygame
import Game, Menu, Sound

class App:
    def __init__(self):
        pygame.init()
        self._running = True
        self._display_surf = None
        self.screenInfo = pygame.display.Info()
        self.screenSize = self.screenWidth, self.screenHeight = self.screenInfo.current_w - 400, self.screenInfo.current_h - 250
        self._display_surf = pygame.display.set_mode(self.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF)  # | pygame.FULLSCREEN)
        pygame.display.set_caption("Trashing and Rushing")
        self.clock = pygame.time.Clock()
        self.clock.tick(27)
        self._running = True
        self.menuVisible = True
        self.menu = Menu.Menu(self._display_surf, self.screenWidth, self.screenHeight)



    def on_init(self):
        pass


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def inMenu(self):
        self.menu.update()
        if self.menu.playClicked:
            self.game = Game.Game(self._display_surf, self.screenSize)
            self.menuVisible = False
        if self.menu.exitClicked:
            self._running = False
            self.menuVisible = False



    def inGame(self):
        self.game.update()

    def on_cleanup(self):
        pass

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            if self.menuVisible:
                self.inMenu()
            if self.menu.playClicked:
                self.inGame()
            pygame.display.update()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()