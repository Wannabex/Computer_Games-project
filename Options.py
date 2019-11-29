import pygame

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

class Options():
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BROWN = (153, 92, 0)
    BLOOD = (128, 0, 0)

    def __init__(self, screen, screenSize):
        self.screen = screen
        self.screenWidth, self.screenHeight = screenSize
        rectWidth = 400
        rectHeight = 100
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 80)
        self.title = self.font.render("           Options      ", True, self.BLOOD)
        self.titleRect = pygame.Rect((self.screenWidth // 4, 10, rectWidth, rectHeight))
        self.configFile = open("./resources/config.txt", 'r')
        self.fileContent = self.configFile.readline()
        if self.fileContent.endswith("True"):
            self.option1Activated = True
        elif self.fileContent.endswith("False"):
            self.option1Activated = False
        self.configFile.close()
        rectWidth = 750
        rectHeight = 55
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 40)
        self.option1Information = self.font.render("    Activate rain effects                      " + str(self.option1Activated), True, self.WHITE)
        self.option1Rect = pygame.Rect((self.screenWidth // 4, self.screenHeight // 3,rectWidth, rectHeight))
        self.option1RectColor = self.BLACK
        rectWidth = 300
        rectHeight = 55
        self.optionsSaveInformation = self.font.render("  Save options    ", True, self.WHITE)
        self.optionsSaveRect = pygame.Rect((self.screenWidth // 3, self.screenHeight - 200, rectWidth, rectHeight))
        self.optionsSaveRectColor = self.BLACK
        self.configChanged = True
        self.optionsExitInformation = self.font.render("    Exit options ", True, self.WHITE)
        self.optionsExitRect = pygame.Rect((self.screenWidth // 2, self.screenHeight - 200, rectWidth, rectHeight))
        self.optionsExitRectColor = self.BLACK
        self.exitOptions = False

        self.mouseClicked = False
        self.mouseCounter = 0
        self.mouseDebounce = 15

    def update(self):
        self.draw()
        mouse = pygame.mouse.get_pos()
        self.mouseClicked = False
        self.mouseCounter += 1
        if self.mouseCounter == self.mouseDebounce:
            mouseClick = pygame.mouse.get_pressed()
            self.mouseClicked = True
            self.mouseCounter = 0
        self.mouseCounter %= self.mouseDebounce
        self.option1RectColor = self.BLACK
        self.optionsSaveRectColor = self.BLACK
        self.optionsExitRectColor = self.BLACK
        if self.option1Rect.x <= mouse[MOUSE_POS_X] <= self.option1Rect.x + self.option1Rect.width and self.option1Rect.y <= mouse[MOUSE_POS_Y] <= self.option1Rect.y + self.option1Rect.height:
            self.option1RectColor = self.BROWN
            if self.mouseClicked and mouseClick[MOUSE_BUTTON_LEFT]:
                self.configChanged = False
                if self.option1Activated:
                    self.fileContent = self.fileContent.replace("True", "False")
                    self.option1Activated = False
                elif not self.option1Activated:
                    self.fileContent = self.fileContent.replace("False", "True")
                    self.option1Activated = True
                self.option1Information = self.font.render("    Activate rain effects                      " + str(self.option1Activated), True, self.WHITE)
        elif self.optionsSaveRect.x <= mouse[MOUSE_POS_X] <= self.optionsSaveRect.x + self.optionsSaveRect.width and self.optionsSaveRect.y <= mouse[MOUSE_POS_Y] <= self.optionsSaveRect.y + self.optionsSaveRect.height:
            self.optionsSaveRectColor = self.BROWN
            if self.mouseClicked and mouseClick[MOUSE_BUTTON_LEFT] and not self.configChanged:
                self.configChanged = True
                self.configFile = open("./resources/config.txt", 'w')
                self.configFile.seek(0, 0)
                self.configFile.write(self.fileContent)
                self.configFile.close()
        elif self.optionsExitRect.x <= mouse[MOUSE_POS_X] <= self.optionsExitRect.x + self.optionsExitRect.width and self.optionsExitRect.y <= mouse[MOUSE_POS_Y] <= self.optionsExitRect.y + self.optionsExitRect.height:
            self.optionsExitRectColor = self.BROWN
            if self.mouseClicked and mouseClick[MOUSE_BUTTON_LEFT]:
                self.exitOptions = True
                self.configFile.close()

    def draw(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.title, self.titleRect)

        pygame.draw.rect(self.screen, self.option1RectColor, self.option1Rect)
        self.screen.blit(self.option1Information, self.option1Rect)

        pygame.draw.rect(self.screen, self.optionsSaveRectColor, self.optionsSaveRect)
        self.screen.blit(self.optionsSaveInformation, self.optionsSaveRect)

        pygame.draw.rect(self.screen, self.optionsExitRectColor, self.optionsExitRect)
        self.screen.blit(self.optionsExitInformation, self.optionsExitRect)


