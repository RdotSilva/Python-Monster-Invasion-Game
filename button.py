import pygame.font

class Button:

    def __init__(self, mi_game, msg):
        # Init button attributes.
        self.screen = mi_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions & properties of button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

