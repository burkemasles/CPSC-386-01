class GameStats():
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        self.game_active = False
        self.high_score_screen_active = False

        self.high_score = 0
        try:
            high_score_file = open('high_score.txt', 'r')
            self.high_score = int(high_score_file.read())
            high_score_file.close()
        except IOError:
            self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
