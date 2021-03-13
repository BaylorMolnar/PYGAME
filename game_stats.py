class GameStats:
    # track stats
    def __init__(self, ai_game):
        # initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        # start game in active state
        self.game_active = False

    def reset_stats(self):
        # initialize changing stats during game
        self.ships_left = self.settings.ship_limit