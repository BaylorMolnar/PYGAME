import pygame


class Ship:
    """class to manage ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)