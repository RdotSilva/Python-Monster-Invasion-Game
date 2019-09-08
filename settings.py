class Settings:
    # Stores all of the settings for the game.

    def __init__(self):
        # Initialize settings

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Archer settings
        self.archer_speed = 1.5

        # Arrow settings
        self.arrow_speed = 1.0
        self.arrow_width = 3
        self.arrow_height = 15
        self.arrow_color = (60, 60, 60)