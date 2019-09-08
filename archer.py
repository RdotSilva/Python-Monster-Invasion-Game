import pygame

class Archer:
    # A class to manage the archer.

    def __init__(self, mi_game):
        # Initialize archer and set its starting position.
        self.screen = mi_game.screen
        self.settings = mi_game.settings
        self.screen_rect = mi_game.screen.get_rect()

        # Load archer image and get its rect.
        self.image = pygame.image.load('images/archer.bmp')
        self.rect = self.image.get_rect()

        # Start each new archer at bottom center of screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for archer's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Update archer position based on movement flag.
        # Update archer x value (not the rect)
        if self.moving_right:
            self.x += self.settings.archer_speed
        if self.moving_left:
            self.x -= self.settings.archer_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        # Draw archer at its current location.
        self.screen.blit(self.image, self.rect)