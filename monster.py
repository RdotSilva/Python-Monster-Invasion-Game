import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    # Class to represent a single monster.

    def __init__(self, mi_game):
        # Initialize the monster and set its starting position.
        super().__init__()
        self.screen = mi_game.screen