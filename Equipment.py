import pygame
from Interface import ActionWheel


MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

ICON_WIDTH = 32
ICON_HEIGHT = 32


class Weapon(pygame.Rect):
    def __init__(self, screen, positionX, positionY, icons, wheel):
        pygame.Rect.__init__(self, (positionX, positionY, ICON_WIDTH, ICON_HEIGHT))
        self.screen = screen
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]
        self.wheelIcon = wheel
        self.name = ""
        self.picked = False
        self.clickable = True
        self.actionsVisible = False

    def update(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:
            self.screen.blit(self.itemHover, self)
            if mouseClick[MOUSE_BUTTON_LEFT] and self.clickable:
                self.actionsVisible = True
        else:
            self.screen.blit(self.itemIdle, self)

    def pickUp(self, weaponX, weaponY):
        self.x = weaponX
        self.y = weaponY
        self.picked = True

    def drop(self, x, y):
        self.x = x
        self.y = y
        self.picked = False

    def wheelEvents(self, clicked):
        if clicked == 0:
            self.actionsVisible = False
        if clicked == 1:
            self.actionsVisible = False
        if clicked == 2:
            self.actionsVisible = False
            return 1
        if clicked == 3:
            self.actionsVisible = False
        if clicked == 4:
            self.actionsVisible = False

    def getName(self):
        return self.name
    
    def getwheelIcon(self):
        return self.wheelIcon


class Sword(Weapon):
    swordIcon = [pygame.image.load("./resources/images/items/weapons/sword1.png"),
                 pygame.image.load("./resources/images/items/weapons/sword2.png")]
    swordWheelIcon = [pygame.image.load("./resources/images/wheel/weapons/sword1.png"),
                 pygame.image.load("./resources/images/wheel/weapons/sword2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.swordIcon, self.swordWheelIcon)
        self.name = "Sword"
        self.description = ""


class Whip(Weapon):
    whipIcon = [pygame.image.load("./resources/images/items/weapons/whip1.png"),
                pygame.image.load("./resources/images/items/weapons/whip2.png")]
    whipWheelIcon = [pygame.image.load("./resources/images/wheel/weapons/whip1.png"),
                 pygame.image.load("./resources/images/wheel/weapons/whip2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.whipIcon, self.whipWheelIcon)
        self.name = "Whip"
        self.description = ""


class Shield(Weapon):
    shieldIcon = [pygame.image.load("./resources/images/items/weapons/shield1.png"),
                  pygame.image.load("./resources/images/items/weapons/shield2.png")]
    shieldWheelIcon = [pygame.image.load("./resources/images/wheel/weapons/shield1.png"),
                 pygame.image.load("./resources/images/wheel/weapons/shield2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.shieldIcon, self.shieldWheelIcon)
        self.name = "Shield"
        self.description = ""

class Consumable(pygame.Rect):
    def __init__(self, screen, positionX, positionY, icons, wheel):
        pygame.Rect.__init__(self, (positionX, positionY, ICON_WIDTH, ICON_HEIGHT))
        self.screen = screen
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]
        self.wheelIcon = wheel
        self.name = ""
        self.picked = False
        self.clickable = True
        self.actionsVisible = False

    def update(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:
            self.screen.blit(self.itemHover, self)
            if mouseClick[MOUSE_BUTTON_LEFT] and self.clickable:
                self.actionsVisible = True
        else:
            self.screen.blit(self.itemIdle, self)

    def pickUp(self, consumableX, consumableY):
        self.x = consumableX
        self.y = consumableY
        self.picked = True

    def drop(self, x, y):
        self.x = x
        self.y = y
        self.picked = False

    def wheelEvents(self, clicked):
        if clicked == 0:
            self.actionsVisible = False
        if clicked == 1:
            self.actionsVisible = False
        if clicked == 2:
            self.actionsVisible = False
            return 1
        if clicked == 3:
            self.actionsVisible = False
        if clicked == 4:
            self.actionsVisible = False

    def getName(self):
        return self.name
    
    def getWheelIcon(self):
        return self.wheelIcon


class Bomb(Consumable):
    bombIcon = [pygame.image.load("./resources/images/items/consumables/bomb1.png"),
                pygame.image.load("./resources/images/items/consumables/bomb2.png")]
    bombWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/bomb1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/bomb2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.bombIcon, self.bombWheelIcon)
        self.name = "Bomb"
        self.description = ""

class Flute(Consumable):
    fluteIcon = [pygame.image.load("./resources/images/items/consumables/flute1.png"),
                pygame.image.load("./resources/images/items/consumables/flute2.png")]
    fluteWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/flute1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/flute2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.fluteIcon, self.fluteWheelIcon)
        self.name = "Flute"
        self.description = ""

class Garlic(Consumable):
    garlicIcon = [pygame.image.load("./resources/images/items/consumables/garlic1.png"),
                pygame.image.load("./resources/images/items/consumables/garlic2.png")]
    garlicWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/garlic1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/garlic2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.garlicIcon, self.garlicWheelIcon)
        self.name = "Garlic"
        self.description = ""

class Rune(Consumable):
    runeIcon = [pygame.image.load("./resources/images/items/consumables/rune1.png"),
                  pygame.image.load("./resources/images/items/consumables/rune2.png")]
    runeWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/rune1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/rune2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.runeIcon, self.runeWheelIcon)
        self.name = "Rune"
        self.description = ""





