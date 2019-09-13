import pygame.font

class Button:

    def __init__(self, mi_game, msg):
        # Init button attributes.
        self.screen = mi_game.screen
        self.screen_rect = self.screen.get_rect()

        
