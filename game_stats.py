class GameStats:
    # Track stats for Monster Invasion Game.

    def __init__(self, mi_game):
        # Init stats
        self.settings = mi_game.settings
        self.reset_stats()
        # Start the game in inactive state.
        self.game_active = False
        #High score never reset
        self.high_score = 0

    def reset_stats(self):
        # Init stats that can change during the game.
        self.lives_left = self.settings.life_limit
        self.score = 0