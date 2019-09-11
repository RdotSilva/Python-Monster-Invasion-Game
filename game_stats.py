class GameStats:
    # Track stats for Monster Invasion Game.

    def __init__(self, mi_game):
        # Init stats
        self.settings = mi_game.settings
        self.reset_stats()