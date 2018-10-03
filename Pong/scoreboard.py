import pygame.font
from pygame.sprite import Group


class Scoreboard():
    def __init__(self, settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        self.text_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = self.screen_rect.top + 30

    def prep_gameover(self):
        score_str = "Game Over"
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.center = self.screen_rect.center

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)