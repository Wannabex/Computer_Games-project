import pygame
import random


class Sound(object):
    def __init__(self):
        pygame.mixer.music.load("./resources/sound/music.mp3")
        pygame.mixer.music.set_volume(0.2)
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

    def thunderstorm(self):
        self.thunderSounds[random.randint(0, 2)].play()
