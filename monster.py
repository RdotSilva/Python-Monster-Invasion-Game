import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    # Class to represent a single monster.

    def __init__(self, mi_game):
        # Initialize the monster and set its starting position.
        super().__init__()
        self.screen = mi_game.screen
        self.settings = mi_game.settings

        # Load the monster image and set its rect attribute.
        self.image = pygame.image.load('images/monster.bmp')
        
        self.rect = self.image.get_rect()

        # Start each new monster near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the monsters exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        # Move the monster to the right.
        self.x += self.settings.monster_speed
        self.rect.x = self.x