import pygame

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

class Menu():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (153, 92, 0)
    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.rectWidth = 335
        self.rectHeight = 60
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 40)
        self.playInformation = self.font.render("    Play new game      ", True, self.WHITE)
        self.optionsInformation = self.font.render("          Options       ", True, self.WHITE)
        self.scoresInformation = self.font.render("  High scores table   ", True, self.WHITE)
        self.exitInformation = self.font.render("      Exit the game     ", True, self.WHITE)
        self.playRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3, self.rectWidth, self.rectHeight))
        self.playRectColor = self.BLACK
        self.optionsRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3 + self.rectHeight, self.rectWidth, self.rectHeight))
        self.optionsRectColor = self.BLACK
        self.scoresRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3 + self.rectHeight * 2, self.rectWidth, self.rectHeight))
        self.scoresRectColor = self.BLACK
        self.exitRect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3 + self.rectHeight * 3, self.rectWidth, self.rectHeight))
        self.exitRectColor = self.BLACK

        self.playClicked = False
        self.optionsClicked = False
        self.scoresClicked = False
        self.exitClicked = False

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
                self.playClicked = True
        elif self.optionsRect.x <= mouse[MOUSE_POS_X] <= self.optionsRect.x + self.optionsRect.width and self.optionsRect.y <= mouse[MOUSE_POS_Y] <= self.optionsRect.y + self.optionsRect.height:
            self.optionsRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.optionsClicked = True
        elif self.scoresRect.x <= mouse[MOUSE_POS_X] <= self.scoresRect.x + self.scoresRect.width and self.scoresRect.y <= mouse[MOUSE_POS_Y] <= self.scoresRect.y + self.scoresRect.height:
            self.scoresRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.scoresClicked = True
        elif self.exitRect.x <= mouse[MOUSE_POS_X] <= self.exitRect.x + self.exitRect.width and self.exitRect.y <= mouse[MOUSE_POS_Y] <= self.exitRect.y + self.exitRect.height:
            self.exitRectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.exitClicked = True

    def draw(self):
        self.screen.fill(self.BLACK)
        pygame.draw.rect(self.screen, self.playRectColor, self.playRect)
        self.screen.blit(self.playInformation, self.playRect)
        pygame.draw.rect(self.screen, self.optionsRectColor, self.optionsRect)
        self.screen.blit(self.optionsInformation, self.optionsRect)
        pygame.draw.rect(self.screen, self.scoresRectColor, self.scoresRect)
        self.screen.blit(self.scoresInformation, self.scoresRect)
        pygame.draw.rect(self.screen, self.exitRectColor, self.exitRect)
        self.screen.blit(self.exitInformation, self.exitRect)
