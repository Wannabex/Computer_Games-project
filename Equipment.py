import pygame


class Weapon(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, ())

    def update(self):
        pass


class Sword(Weapon):
    def __init__(self):
        Weapon.__init__()

    def update(self):
        pass


class Whip(Weapon):
    def __init__(self):
        Weapon.__init__()

    def update(self):
        pass


class Shield(Weapon):
    def __init__(self):
        Weapon.__init__()

    def update(self):
        pass






class Consumable(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, ())

    def update(self):
        pass


class Bomb(Consumable):
    def __init__(self):
        Consumable.__init__()

    def update(self):
        pass


class Flute(Consumable):
    def __init__(self):
        Consumable.__init__()

    def update(self):
        pass


class Garlic(Consumable):
    def __init__(self):
        Consumable.__init__()

    def update(self):
        pass


class Rune(Consumable):
    def __init__(self):
        Consumable.__init__()

    def update(self):
        pass





