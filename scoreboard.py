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
        self.prep_high_score()

    def prep_high_score(self):
        # Turn the high score into a rendered image.
        high_score = round(self.stats.high_score, -1)
        high_score_str ="{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

    def prep_score(self):
        # Turn the score into a rendered image.
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at top right of screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        # Draw score to screen.
        self.screen.blit(self.score_image, self.score_rect)