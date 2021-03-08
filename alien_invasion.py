import sys
import pygame


class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main loop for game"""

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw screen during each pass through loop
            self.screen.fill(self.bg_color)
            # make most recent screen visible
            pygame.display.flip()


if __name__ == "__main__":
    # make game instance
    ai = AlienInvasion()
    ai.run_game()