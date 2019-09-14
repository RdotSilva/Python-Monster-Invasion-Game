import pygame.font

class Scoreboard:
    # Class to report scoring info.

    def __init__(self, mi_game):
        # Initialize scorekeeping attributes.
        self.screen = mi_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = mi_game.settings
        self.stats = mi_game.stats

        # Font settings for scoring info.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score image.
        self.prep_score()

    def prep_score(self):
        # Turn the score into a rendered image.
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)