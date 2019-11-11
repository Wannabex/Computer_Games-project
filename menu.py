import pygame
import Sound

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

class Menu():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (153, 92, 0)
    BLOOD = (128, 0, 0)

    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        rectWidth = 400
        rectHeight = 100
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 80)
        self.title = self.font.render("         TRASHING  &  RUSHING    ", True, self.BLOOD)
        self.titleRect = pygame.Rect((10, 10, rectWidth, rectHeight))
        rectWidth = 335
        rectHeight = 55
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 40)
        self.playInformation = self.font.render("    Play new game      ", True, self.WHITE)
        self.optionsInformation = self.font.render("          Options       ", True, self.WHITE)
        self.scoresInformation = self.font.render("  High scores table   ", True, self.WHITE)
        self.exitInformation = self.font.render("      Exit the game     ", True, self.WHITE)
        self.playRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3, rectWidth, rectHeight))
        self.playRectColor = self.BLACK
        self.optionsRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3 + rectHeight, rectWidth, rectHeight))
        self.optionsRectColor = self.BLACK
        self.scoresRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3 + rectHeight * 2, rectWidth, rectHeight))
        self.scoresRectColor = self.BLACK
        self.exitRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3 + rectHeight * 3, rectWidth, rectHeight))
        self.exitRectColor = self.BLACK
        self.playActivated = False
        self.optionsActivated = False
        self.scoresActivated = False
        self.exitActivated = False
        self.startMenuMusic()

    def update(self):
        self.draw()
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        self.playRectColor = self.BLACK
        self.optionsRectColor = self.BLACK
        self.scoresRectColor = self.BLACK
        self.exitRectColor = self.BLACK
        if self.playRect.x <= mouse[MOUSE_POS_X] <= self.playRect.x + self.playRect.width and self.playRect.y <= mouse[MOUSE_POS_Y] <= self.playRect.y + self.playRect.height:
            self.playRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.playActivated = True
                pygame.mixer.music.stop()
        elif self.optionsRect.x <= mouse[MOUSE_POS_X] <= self.optionsRect.x + self.optionsRect.width and self.optionsRect.y <= mouse[MOUSE_POS_Y] <= self.optionsRect.y + self.optionsRect.height:
            self.optionsRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.optionsActivated = True
        elif self.scoresRect.x <= mouse[MOUSE_POS_X] <= self.scoresRect.x + self.scoresRect.width and self.scoresRect.y <= mouse[MOUSE_POS_Y] <= self.scoresRect.y + self.scoresRect.height:
            self.scoresRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.scoresActivated = True
        elif self.exitRect.x <= mouse[MOUSE_POS_X] <= self.exitRect.x + self.exitRect.width and self.exitRect.y <= mouse[MOUSE_POS_Y] <= self.exitRect.y + self.exitRect.height:
            self.exitRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.exitActivated = True

    def draw(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.title, self.titleRect)
        pygame.draw.rect(self.screen, self.playRectColor, self.playRect)
        self.screen.blit(self.playInformation, self.playRect)
        pygame.draw.rect(self.screen, self.optionsRectColor, self.optionsRect)
        self.screen.blit(self.optionsInformation, self.optionsRect)
        pygame.draw.rect(self.screen, self.scoresRectColor, self.scoresRect)
        self.screen.blit(self.scoresInformation, self.scoresRect)
        pygame.draw.rect(self.screen, self.exitRectColor, self.exitRect)
        self.screen.blit(self.exitInformation, self.exitRect)

    def startMenuMusic(self):
        pygame.mixer.music.load("./resources/sound/menu.mp3")
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)