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

    def _check_events(self):
        # Watch for keyboard/mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Respond to keypresses.
        if event.key == pygame.K_RIGHT:
            self.archer.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.archer.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # Response to key releases
        if event.key == pygame.K_RIGHT:
            self.archer.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.archer.moving_left = False

    def _update_screen(self):
        # Redraw the screen during each pass of the loop.
        self.screen.fill(self.settings.bg_color)
        self.archer.blitme()

        # Make most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        # Start the main game loop.
        while True:
            self._check_events()
            self.archer.update()
            self._update_screen()

if __name__ == '__main__':
    # Make a game instance & run the game.
    mi = MonsterInvasion()
    mi.run_game()