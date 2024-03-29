import pygame
import Menu
import Game
import Options


class App:
    def __init__(self):
        pygame.init()
        self._running = True
        self._display_surf = None
        self.screenInfo = pygame.display.Info()
        self.screenSize = self.screenWidth, self.screenHeight = 1366, 768 #self.screenInfo.current_w , self.screenInfo.current_h
        self._display_surf = pygame.display.set_mode(self.screenSize, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        pygame.display.set_caption("Trashing and Rushing")
        self.clock = pygame.time.Clock()
        self.clock.tick(216)
        self._running = True
        self.menuVisible = True
        self.menu = Menu.Menu(self._display_surf, self.screenWidth, self.screenHeight)

    def on_init(self):
        pass

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def inGame(self):
        self.game.update()
        if self.game.exitGame:
            self.menu.playActivated = False
            self.menuVisible = True
            self.menu.startMenuMusic()
            del self.game

    def inMenu(self):
        self.menu.update()
        if self.menu.playActivated:
            self.game = Game.Game(self._display_surf, self.screenSize)
            self.menuVisible = False
        elif self.menu.optionsActivated:
            self.options = Options.Options(self._display_surf, self.screenSize)
            self.menuVisible = False
        elif self.menu.exitActivated:
            self._running = False
            self.menuVisible = False

    def inOptions(self):
        self.options.update()
        if self.options.exitOptions:
            self.menu.optionsActivated = False
            self.menuVisible = True
            del self.options

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
            elif self.menu.playActivated:
                self.inGame()
            elif self.menu.optionsActivated:
                self.inOptions()
            pygame.display.update()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()