import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    # Class to manage arrows shot by archer.

    def __init__(self, mi_game):
        # Create an arrow object at the archer's current position.
        super().__init__()
        self.screen = mi_game.screen
        self.settings = mi_game.settings
        self.color = self.settings.arrow_color

        # Create an arrow react at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.arrow_width, self.settings.arrow_height)
        self.rect.midtop = mi_game.archer.rect.midtop

        # Store the arrow's position as decimal value.
        self.y = float(self.rect.y)

    def update(self):
        # Move arrow up screen.
        # Update the decimal position of arrow.
        self.y -= self.settings.arrow_speed
        
        #update rect position.
        self.rect.y = self.y

    def draw_arrow(self):
        # Draw the arrow to screen.
        pygame.draw.rect(self.screen, self.color, self.rect)