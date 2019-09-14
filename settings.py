class Settings:
    # Stores all of the settings for the game.

    def __init__(self):
        # Initialize static settings

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Archer settings
        self.archer_speed = 1.5
        self.life_limit = 3

        # Arrow settings
        self.arrow_speed = 1.5
        self.arrow_width = 300
        self.arrow_height = 15
        self.arrow_color = (60, 60, 60)
        self.arrows_allowed = 3

        # Monster settings
        self.monster_speed = 1.0
        self.horde_drop_speed = 10
        

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize settings that change through the game.
        self.archer_speed = 1.5
        self.arrow_speed = 3.0
        self.monster_speed = 1.0

        # horde_direction of 1 represents right; -1 represents left.
        self.horde_direction = 1

    def increase_speed(self):
        # Increase speed settings
        self.archer_speed *= self.speedup_scale
        self.arrow_speed *= self.speedup_scale
        self.monster_speed *= self.speedup_scale