import sys

import pygame

from settings import Settings
from archer import Archer

class MonsterInvasion:
  # Class for game assets/behavior.

  def __init__(self):
      # Init the game & create resources.
      pygame.init()
      self.settings = Settings()

      self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
      pygame.display.set_caption("Monster Invasion")

      self.archer = Archer(self)

  def run_game(self):
      # Start the main game loop.
      while True:
        # Watch for keyboard/mouse events.
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            sys.exit()

          # Redraw the screen during each pass of the loop.
          self.screen.fill(self.settings.bg_color)
          self.archer.blitme()

          # Make most recently drawn screen visible.
          pygame.display.flip()

if __name__ == '__main__':
  # Make a game instance & run the game.
  mi = MonsterInvasion()
  mi.run_game()