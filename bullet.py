import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        # create bullet at ships current position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create at 0,0 then set to correct
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet as decimal
        self.y = float(self.rect.y)

    def update(self):
        # move bullet up screen
        # update decimal postion
        self.y -= self.settings.bullt_speed
        # update rect
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullet
        pygame.draw.rect(self.screen, self.color, self.rect)