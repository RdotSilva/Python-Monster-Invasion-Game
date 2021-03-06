import pygame.font
from pygame.sprite import Group
from archer import Archer


class Scoreboard:
    # Class to report scoring info.

    def __init__(self, mi_game):
        # Initialize scorekeeping attributes.
        self.mi_game = mi_game
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
        self.prep_level()
        self.prep_archers()

    def prep_high_score(self):
        # Turn the high score into a rendered image.
        high_score = round(self.stats.high_score, -1)
        high_score_str ="{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at top of screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

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
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.archers.draw(self.screen)

    def check_high_score(self):
        # Check to see if there's a new high score.
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        # Turn the level into a rendered image.
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_archers(self):
        # Show how many archer are left.
        self.archers = Group()
        for archer_number in range(self.stats.lives_left):
            archer = Archer(self.mi_game)
            archer.rect.x = 10 + archer_number * archer.rect.width
            archer.rect.y = 10
            self.archers.add(archer)