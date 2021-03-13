import pygame


class Ship:
    """class to manage ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # start ship at bottom
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # update ships x not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect from self.x
        self.rect.x = self.x

    def blitme(self):
        # draw ship at current location
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # center ship
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)