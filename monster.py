import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    # Class to represent a single monster.

    def __init__(self, mi_game):
        # Initialize the monster and set its starting position.
        super().__init__()
        self.screen = mi_game.screen

        # Load the monster image and set its rect attribute.
        self.image = pygame.image.load('/images/monster.bmp')
        self.rect = self.image.get_rect()