class Settings:
    """Class to store all settings"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # bullets
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # alien settings
        self.alien_speed = 1.0
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        # how quickly game speeds up
        self.speedup_scale = 1.1
        # how quickly alien point value increases
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # initialize setting that change throughout game
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction 0f 1 is right and -1 is left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        # increase speed setting and point values
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
