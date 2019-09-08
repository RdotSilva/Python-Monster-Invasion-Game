import sys

import pygame


class MonsterInvasion:
  # Class for game assets/behavior.

def __init__(self):
    # Init the game & create resources.
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Monster Invasion")
