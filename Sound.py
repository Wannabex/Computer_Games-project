import pygame
import random


class Sound(object):
    def __init__(self):
        pygame.mixer.music.load("./resources/sound/music.mp3")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)
        self.ambience = pygame.mixer.Sound("./resources/sound/rain_ambience.wav")
        self.ambience.set_volume(0.8)
        self.ambience.play(-1)
        self.thunderSounds = []
        thunder1 = pygame.mixer.Sound("./resources/sound/thunder1.wav")
        thunder2 = pygame.mixer.Sound("./resources/sound/thunder2.wav")
        thunder3 = pygame.mixer.Sound("./resources/sound/thunder3.wav")
        self.thunderSounds.append(thunder1)
        self.thunderSounds.append(thunder2)
        self.thunderSounds.append(thunder3)
        self.monsterSounds = []
        roar1 = pygame.mixer.Sound("./resources/sound/roar1.wav")
        roar2 = pygame.mixer.Sound("./resources/sound/roar2.wav")
        roar3 = pygame.mixer.Sound("./resources/sound/roar3.wav")
        self.monsterSounds.append(roar1)
        self.monsterSounds.append(roar2)
        self.monsterSounds.append(roar3)


    def thunderstorm(self):
        self.thunderSounds[random.randint(0, 2)].play()

    def monsterRoar(self):
        self.monsterSounds[random.randint(0, 2)].play()
