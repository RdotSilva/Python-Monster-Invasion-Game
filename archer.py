import pygame

class Archer:
    # A class to manage the archer.

    def __init__(self, mi_game):
        # Initialize archer and set its starting position.
        self.screen = mi_game.screen
        self.screen_rect = mi_game.screen.get_rect()

        # Load archer image and get its rect.
        self.image = pygame.image.load('images/archer.bmp')
        self.rect = self.image.get_rect()

        # Start each new archer at bottom center of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False

    def update(self):
        # Update archer position based on movement flag.
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        # Draw archer at its current location.
        self.screen.blit(self.image, self.rect)