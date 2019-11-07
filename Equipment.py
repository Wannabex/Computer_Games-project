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
    def __init__(self, screen, positionX, positionY, icons):
        pygame.Rect.__init__(self, (positionX, positionY, ICON_WIDTH, ICON_HEIGHT))
        self.screen = screen
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]
        self.name = ""
        self.picked = False
        self.actions = ActionWheel(screen, positionX - ActionWheel.WHEEL_WIDTH - 3, positionY - ActionWheel.WHEEL_HEIGHT - 3)
        self.actions.setActionWheel(upIcon= self.itemIdle, downIcon=self.itemHover, rightIcon=self.itemIdle)
        self.actionsVisible = False

    def update(self):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()
        if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:
            self.screen.blit(self.itemHover, self)
            if mouseClick[MOUSE_BUTTON_LEFT]:
                self.actionsVisible = True
        else:
            self.screen.blit(self.itemIdle, self)
        if self.actionsVisible:
            self.actions.update()

    def pickUp(self, weaponX, weaponY):
        self.x = weaponX
        self.y = weaponY
        self.picked = True

    def drop(self, x, y):
        self.x = x
        self.y = y
        self.picked = False

    def getName(self):
        return self.name


class Sword(Weapon):
    swordIcon = [pygame.image.load("./resources/images/items/weapons/sword1.png"),
                 pygame.image.load("./resources/images/items/weapons/sword2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.swordIcon)
        self.name = "Sword"


class Whip(Weapon):
    whipIcon = [pygame.image.load("./resources/images/items/weapons/whip1.png"),
                pygame.image.load("./resources/images/items/weapons/whip2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.whipIcon)
        self.name = "Whip"



class Shield(Weapon):
    shieldIcon = [pygame.image.load("./resources/images/items/weapons/shield1.png"),
                  pygame.image.load("./resources/images/items/weapons/shield2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.shieldIcon)
        self.name = "Shield"



class Consumable(pygame.Rect):
    def __init__(self, screen, positionX, positionY, icons):
        pygame.Rect.__init__(self, (positionX, positionY, ICON_WIDTH, ICON_HEIGHT))
        self.screen = screen
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]
        self.name = ""
        self.picked = False

    def update(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height and not self.picked:
            self.screen.blit(self.itemHover, self)
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

    def getName(self):
        return self.name

class Bomb(Consumable):
    bombIcon = [pygame.image.load("./resources/images/items/consumables/bomb1.png"),
                pygame.image.load("./resources/images/items/consumables/bomb2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.bombIcon)
        self.name = "Bomb"


class Flute(Consumable):
    fluteIcon = [pygame.image.load("./resources/images/items/consumables/flute1.png"),
                pygame.image.load("./resources/images/items/consumables/flute2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.fluteIcon)
        self.name = "Flute"


class Garlic(Consumable):
    garlicIcon = [pygame.image.load("./resources/images/items/consumables/garlic1.png"),
                pygame.image.load("./resources/images/items/consumables/garlic2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.garlicIcon)
        self.name = "Garlic"


class Rune(Consumable):
    runeIcon = [pygame.image.load("./resources/images/items/consumables/rune1.png"),
                  pygame.image.load("./resources/images/items/consumables/rune2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.runeIcon)
        self.name = "Rune"






