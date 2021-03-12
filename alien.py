import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # represents single alien in fleet
    def __init__(self, ai_game):
        # initialize alien and start position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien image
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # start near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien horizontal
        self.x = float(self.rect.x)

    def check_edges(self):
        # true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # move alien to right
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
