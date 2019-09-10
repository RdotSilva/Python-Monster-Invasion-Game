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

    def check_edges(self):
        # Return True if monster is at edge of screen.
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # Move the monster left or right.
        self.x += (self.settings.monster_speed * self.settings.horde_direction)
        self.rect.x = self.x