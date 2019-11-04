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
    def __init__(self):
        pygame.Rect.__init__(self, ())


class Bomb(Consumable):
    def __init__(self):
        Consumable.__init__()


class Flute(Consumable):
    def __init__(self):
        Consumable.__init__()



class Garlic(Consumable):
    def __init__(self):
        Consumable.__init__()



class Rune(Consumable):
    def __init__(self):
        Consumable.__init__()






