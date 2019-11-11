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

    def __init__(self, screen, screenWidth, screenHeight):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.rectWidth = 400
        self.rectHeight = 100
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 80)
        self.title = self.font.render("           Options      ", True, self.BLOOD)
        self.titleRect = pygame.Rect((10, 10, self.rectWidth, self.rectHeight))
        self.configFile = open("./resources/config.txt", 'r')
        fileContent = self.configFile.readlines()
        self.option1Activated = False
        self.rectWidth = 335
        self.rectHeight = 55
        self.font = pygame.font.Font("./resources/other/gothic.ttf", 40)
        self.option1Information = self.font.render("    Activate rain effects        " + str(self.option1Activated), True, self.WHITE)
        self.option1Rect = pygame.Rect((3 * self.screenWidth // 8, self.screenHeight // 3, self.rectWidth, self.rectHeight))
        self.playRectColor = self.BLACK



    def update(self):
        self.draw()
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        self.option1RectColor = self.BLACK
        if self.option1Rect.x <= mouse[MOUSE_POS_X] <= self.option1Rect.x + self.option1Rect.width and self.option1Rect.y <= mouse[MOUSE_POS_Y] <= self.option1Rect.y + self.option1Rect.height:
            self.option1RectColor = self.BROWN
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.option1Activated = True


    def draw(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.title, self.titleRect)

        pygame.draw.rect(self.screen, self.option1RectColor, self.option1Rect)
        self.screen.blit(self.option1Information, self.option1Rect)


