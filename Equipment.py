import pygame


MOUSE_POS_X = 0
MOUSE_POS_Y = 1

ICON_WIDTH = 32
ICON_HEIGHT = 32


class Weapon(pygame.Rect):
    def __init__(self, screen, positionX, positionY, icons):
        pygame.Rect.__init__(self, (positionX, positionY, ICON_WIDTH, ICON_HEIGHT))
        self.screen = screen
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]

    def update(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height:
            self.screen.blit(self.itemHover, self)
        else:
            self.screen.blit(self.itemIdle, self)


class Sword(Weapon):
    swordIcon = [pygame.image.load("./resources/images/items/weapons/sword1.png"),
                 pygame.image.load("./resources/images/items/weapons/sword2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.swordIcon)


class Whip(Weapon):
    whipIcon = [pygame.image.load("./resources/images/items/weapons/whip1.png"),
                pygame.image.load("./resources/images/items/weapons/whip2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.whipIcon)



class Shield(Weapon):
    shieldIcon = [pygame.image.load("./resources/images/items/weapons/shield1.png"),
                  pygame.image.load("./resources/images/items/weapons/shield2.png")]

    def __init__(self, screen, positionX, positionY):
        Weapon.__init__(self, screen, positionX, positionY, self.shieldIcon)



class Consumable(pygame.Rect):
    def __init__(self, screen, positionX, positionY, icons):
        pygame.Rect.__init__(self, (positionX, positionY, ICON_WIDTH, ICON_HEIGHT))
        self.screen = screen
        self.itemIcons = icons
        self.itemIdle = icons[1]
        self.itemHover = icons[0]

    def update(self):
        mouse = pygame.mouse.get_pos()
        if self.x <= mouse[MOUSE_POS_X] <= self.x + self.width and self.y <= mouse[MOUSE_POS_Y] <= self.y + self.height:
            self.screen.blit(self.itemHover, self)
        else:
            self.screen.blit(self.itemIdle, self)

class Bomb(Consumable):
    bombIcon = [pygame.image.load("./resources/images/items/consumables/bomb1.png"),
                pygame.image.load("./resources/images/items/consumables/bomb2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.bombIcon)


class Flute(Consumable):
    fluteIcon = [pygame.image.load("./resources/images/items/consumables/flute1.png"),
                pygame.image.load("./resources/images/items/consumables/flute2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.fluteIcon)


class Garlic(Consumable):
    garlicIcon = [pygame.image.load("./resources/images/items/consumables/garlic1.png"),
                pygame.image.load("./resources/images/items/consumables/garlic2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.garlicIcon)


class Rune(Consumable):
    runeIcon = [pygame.image.load("./resources/images/items/consumables/rune1.png"),
                  pygame.image.load("./resources/images/items/consumables/rune2.png")]

    def __init__(self, screen, positionX, positionY):
        Consumable.__init__(self, screen, positionX, positionY, self.runeIcon)






