import pygame

class Archer:
  # A class to manage the archer.

  def __init__(self, ai_game):
    # Initialize archer and set its starting position.
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()

    # Load archer image and get its rect.
    self.image = pygame.image.load('images/archer.bmp')
    self.rect = self.image.get_rect()

    # Start each new archer at bottom center of screen.
    self.rect.modbottom = self.screen_rect.midbottom