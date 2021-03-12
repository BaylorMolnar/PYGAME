import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # represents single alien in fleet
    def __init__(self, ai_game):
        # initialize alien and start position
        super().__init__()
        self.screen = ai_game.screen

        # load alien image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien horizontal
        self.x = float(self.rect.x)