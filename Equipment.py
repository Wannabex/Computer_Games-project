import pygame
import Building
import random

MOUSE_POS_X = 0
MOUSE_POS_Y = 1

MOUSE_BUTTON_LEFT = 0
MOUSE_BUTTON_MIDDLE = 1
MOUSE_BUTTON_RIGHT = 2

ICON_WIDTH = 32
ICON_HEIGHT = 32


class Weapon(pygame.Rect):
    def __init__(self, screen, building, icons, wheel):
        self.building = building
        self.screen = screen
        pygame.Rect.__init__(self, (0, 0, ICON_WIDTH, ICON_HEIGHT))
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]
        self.wheelIcon = wheel
        self.name = ""
        self.picked = False
        self.clickable = True
        self.actionsVisible = False
        self.descriptionShowed = False
        self.destroyed = False

    def spawn(self):
        self.building.spawnObject(self)

    def update(self):
        if not self.destroyed:
            mouse = pygame.mouse.get_pos()
            mouseClick = pygame.mouse.get_pressed()
            if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:
                self.screen.blit(self.itemHover, self)
                if mouseClick[MOUSE_BUTTON_LEFT] and self.clickable:
                    self.actionsVisible = True
            else:
                self.screen.blit(self.itemIdle, self)
        else:
            del self

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

    def showDescription(self):
        descriptionShowed = True


class Sword(Weapon):
    swordIcon = [pygame.image.load("./resources/images/items/weapons/sword1.png"),
                 pygame.image.load("./resources/images/items/weapons/sword2.png")]
    swordWheelIcon = [pygame.image.load("./resources/images/wheel/weapons/sword1.png"),
                 pygame.image.load("./resources/images/wheel/weapons/sword2.png")]

    def __init__(self, screen, building):
        Weapon.__init__(self, screen, building, self.swordIcon, self.swordWheelIcon)
        self.name = "Sword"
        self.description = "Very pointy"


class Whip(Weapon):
    whipIcon = [pygame.image.load("./resources/images/items/weapons/whip1.png"),
                pygame.image.load("./resources/images/items/weapons/whip2.png")]
    whipWheelIcon = [pygame.image.load("./resources/images/wheel/weapons/whip1.png"),
                 pygame.image.load("./resources/images/wheel/weapons/whip2.png")]

    def __init__(self, screen, building):
        Weapon.__init__(self, screen, building, self.whipIcon, self.whipWheelIcon)
        self.name = "Whip"
        self.description = "Can hurt people"


class Shield(Weapon):
    shieldIcon = [pygame.image.load("./resources/images/items/weapons/shield1.png"),
                  pygame.image.load("./resources/images/items/weapons/shield2.png")]
    shieldWheelIcon = [pygame.image.load("./resources/images/wheel/weapons/shield1.png"),
                 pygame.image.load("./resources/images/wheel/weapons/shield2.png")]

    def __init__(self, screen, building):
        Weapon.__init__(self, screen, building, self.shieldIcon, self.shieldWheelIcon)
        self.name = "Shield"
        self.description = "Good for protection and bashing"

class Consumable(pygame.Rect):
    def __init__(self, screen, building, icons, wheel):
        self.building = building
        self.screen = screen
        pygame.Rect.__init__(self, (0, 0, ICON_WIDTH, ICON_HEIGHT))
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]
        self.wheelIcon = wheel
        self.name = ""
        self.picked = False
        self.clickable = True
        self.actionsVisible = False
        self.destroyed = False

    def spawn(self):
        self.building.spawnObject(self)

    def update(self):
        if not self.destroyed:
            mouse = pygame.mouse.get_pos()
            mouseClick = pygame.mouse.get_pressed()
            if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:
                self.screen.blit(self.itemHover, self)
                if mouseClick[MOUSE_BUTTON_LEFT] and self.clickable:
                    self.actionsVisible = True
            else:
                self.screen.blit(self.itemIdle, self)
        else:
            del self

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

    def __init__(self, screen, building):
        Consumable.__init__(self, screen, building, self.bombIcon, self.bombWheelIcon)
        self.name = "Bomb"
        self.description = "Bomb goes boom"

class Flute(Consumable):
    fluteIcon = [pygame.image.load("./resources/images/items/consumables/flute1.png"),
                pygame.image.load("./resources/images/items/consumables/flute2.png")]
    fluteWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/flute1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/flute2.png")]

    def __init__(self, screen, building):
        Consumable.__init__(self, screen, building, self.fluteIcon, self.fluteWheelIcon)
        self.name = "Flute"
        self.description = "Flute plays music"

class Garlic(Consumable):
    garlicIcon = [pygame.image.load("./resources/images/items/consumables/garlic1.png"),
                pygame.image.load("./resources/images/items/consumables/garlic2.png")]
    garlicWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/garlic1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/garlic2.png")]

    def __init__(self, screen, building):
        Consumable.__init__(self, screen, building, self.garlicIcon, self.garlicWheelIcon)
        self.name = "Garlic"
        self.description = "Garlic is strong against vampires"

class Rune(Consumable):
    runeIcon = [pygame.image.load("./resources/images/items/consumables/rune1.png"),
                  pygame.image.load("./resources/images/items/consumables/rune2.png")]
    runeWheelIcon = [pygame.image.load("./resources/images/wheel/consumables/rune1.png"),
                 pygame.image.load("./resources/images/wheel/consumables/rune2.png")]

    def __init__(self, screen, building):
        Consumable.__init__(self, screen, building, self.runeIcon, self.runeWheelIcon)
        self.name = "Rune"
        self.description = "Rune can teleport things"





