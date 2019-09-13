import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from archer import Archer
from arrow import Arrow
from monster import Monster

class MonsterInvasion:
    # Class for game assets/behavior.

    def __init__(self):
        # Init the game & create resources.
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Monster Invasion")

        # Create instance to store game stats.
        self.stats = GameStats(self)

        self.archer = Archer(self)
        self.arrows = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()

        self._create_horde()

        # Create a play button.
        self.play_button = Button(self, "Play")

    def _create_horde(self):
        # Create a horde of monsters.
        # Make a monster and find the number of monsters in a row.
        # Spacing between each monster is equal to one monster width.
        monster = Monster(self)
        monster_width, monster_height = monster.rect.size
        available_space_x = self.settings.screen_width - (2 * monster_width)
        number_monsters_x = available_space_x // (2 * monster_width)

        # Determine the number of rows of monsters that fit on the screen.
        archer_height = self.archer.rect.height
        available_space_y = (self.settings.screen_height - (3 * monster_height) - archer_height)

        number_rows = available_space_y // (2 * monster_height)

        # Create full horde of monsters.
        for row_number in range(number_rows):
            for monster_number in range(number_monsters_x):
                self._create_monster(monster_number, row_number)

    def _create_monster(self, monster_number, row_number):
        # Create a monster and place it in a row.
        monster = Monster(self)
        monster_width, monster_height = monster.rect.size
        monster.x = monster_width + 2 * monster_width * monster_number
        monster.rect.x = monster.x
        monster.rect.y = monster.rect.height + 2 * monster.rect.height * row_number
        self.monsters.add(monster)

    def _update_monsters(self):
        # Check if horde is at edge, then update the positions of all monsters in the horde.
        self._check_horde_edges()
        self.monsters.update()

        # Look for monster-archer collisions.
        if pygame.sprite.spritecollideany(self.archer, self.monsters):
            self._archer_hit()

        # Look for monsters hitting the bottom of screen.
        self._check_monsters_bottom()

    def _check_horde_edges(self):
        # Respond appropriately if monsters have reached an edge of screen.
        for monster in self.monsters.sprites():
            if monster.check_edges():
                self._change_horde_direction()
                break

    def _check_monsters_bottom(self):
        # Check if any monsters have reached the bottom of the screen.
        screen_rect = self.screen.get_rect()
        for monster in self.monsters.sprites():
            if monster.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if archer got hit.
                self._archer_hit()
                break

    def _change_horde_direction(self):
        # Drop the entire horde and change horde direction.
        for monster in self.monsters.sprites():
            monster.rect.y += self.settings.horde_drop_speed
        self.settings.horde_direction *= -1
        
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
        elif event.key == pygame.K_SPACE:
            self._fire_arrow()

    def _check_keyup_events(self, event):
        # Response to key releases
        if event.key == pygame.K_RIGHT:
            self.archer.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.archer.moving_left = False

    def _fire_arrow(self):
        # Create new arrow and add to arrow group.
        if len(self.arrows) < self.settings.arrows_allowed:
            new_arrow = Arrow(self)
            self.arrows.add(new_arrow)

    def _update_arrows(self):
        # Update position of arrows & get rid of old arrows.
        # Update arrow positions.
        self.arrows.update()

        # Get rid of arrows once they are off screen.
        for arrow in self.arrows.copy():
            if arrow.rect.bottom <= 0:
                self.arrows.remove(arrow)
        self._check_arrow_monster_collisions()

    def _check_arrow_monster_collisions(self):
        # Respond to arrow-monster collisions.
        # Remove any arrows/monsters that have collided.
        collisions = pygame.sprite.groupcollide(self.arrows, self.monsters, True, True)

        if not self.monsters:
            # Destroy existing arrows & create new horde.
            self.arrows.empty()
            self._create_horde()

    def _archer_hit(self):
        # Respond to the archer being hit by a monster.
        if self.stats.lives_left > 0:
            # Decrement lives_left.
            self.stats.lives_left -= 1

            # Get rid of any remaining monsters/arrows.
            self.monsters.empty()
            self.arrows.empty()

            # Create a new horde & center the archer.
            self._create_horde()
            self.archer.center_archer()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_screen(self):
        # Redraw the screen during each pass of the loop.
        self.screen.fill(self.settings.bg_color)
        self.archer.blitme()

        for arrow in self.arrows.sprites():
            arrow.draw_arrow()
        self.monsters.draw(self.screen)

        # Draw the play button if game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make most recently drawn screen visible.
        pygame.display.flip()

    def run_game(self):
        # Start the main game loop.
        while True:
            self._check_events()

            if self.stats.game_active:
                self.archer.update()
                self._update_arrows()
                self._update_monsters()

            self._update_screen()

if __name__ == '__main__':
    # Make a game instance & run the game.
    mi = MonsterInvasion()
    mi.run_game()