import pygame
from button import Button


class Start_Screen():
    """Class for all of the start screen stuff"""

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.title_color = (0, 255, 0)
        self.color = (230, 230, 230)
        self.title_font = pygame.font.SysFont(None, 96)
        self.font = pygame.font.SysFont(None, 48)

    def prep_title(self):

        self.title_image = self.font.render("Space Invaders", True, self.title_color, self.ai_settings.start_color)
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.top = self.screen_rect.top + 30

    def prep_high_score_screen(self, stats):
        self.high_score_image = self.font.render(str(stats.high_score), True, self.title_color, self.ai_settings.start_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.center = self.screen_rect.center

    def prep_small_alien(self):
        self.small_image = pygame.image.load('images/Small Alien.png')
        self.small_rect = self.small_image.get_rect()
        self.small_rect.centerx = self.screen_rect.centerx - 50
        self.small_rect.centery = self.screen_rect.centery + 60

    def prep_medium_alien(self):
        self.medium_image = pygame.image.load('images/Medium AlienV5.png')
        self.medium_rect = self.medium_image.get_rect()
        self.medium_rect.centerx = self.screen_rect.centerx - 50
        self.medium_rect.centery = self.screen_rect.centery + 120

    def prep_big_alien(self):
        self.big_image = pygame.image.load('images/Big Alien.png')
        self.big_rect = self.big_image.get_rect()
        self.big_rect.centerx = self.screen_rect.centerx - 50
        self.big_rect.centery = self.screen_rect.centery + 180

    def prep_alien_scores(self):
        self.small_alien_image = self.font.render("10", True, self.color, self.ai_settings.start_color)
        self.small_alien_rect = self.small_alien_image.get_rect()
        self.small_alien_rect.centerx = self.screen_rect.centerx + 50
        self.small_alien_rect.centery = self.screen_rect.centery + 60

        self.medium_alien_image = self.font.render("20", True, self.color, self.ai_settings.start_color)
        self.medium_alien_rect = self.medium_alien_image.get_rect()
        self.medium_alien_rect.centerx = self.screen_rect.centerx + 50
        self.medium_alien_rect.centery = self.screen_rect.centery + 120

        self.big_alien_image = self.font.render("40", True, self.color, self.ai_settings.start_color)
        self.big_alien_rect = self.big_alien_image.get_rect()
        self.big_alien_rect.centerx = self.screen_rect.centerx + 50
        self.big_alien_rect.centery = self.screen_rect.centery + 180

    def prep_high_score_button(self):
        self.button = Button(self.screen, "High Score", self.screen_rect.centerx, self.screen_rect.centery + 240)

    def show_high_score_screen(self):
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def show_start_screen(self):
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.small_image, self.small_rect)
        self.screen.blit(self.medium_image, self.medium_rect)
        self.screen.blit(self.big_image, self.big_rect)
        self.screen.blit(self.small_alien_image, self.small_alien_rect)
        self.screen.blit(self.medium_alien_image, self.medium_alien_rect)
        self.screen.blit(self.big_alien_image, self.big_alien_rect)
        self.button.draw_button()