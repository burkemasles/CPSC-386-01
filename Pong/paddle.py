import pygame


class Paddle():
    def __init__(self, settings, screen, orientation):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load
        if orientation == "Left" or "Right":
            self.width, self.height = 25, 150
        elif orientation == "Bottom":
            self.width, self.height = 150, 25
        self.paddle_color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        if orientation == "Left":
            self.rect.centery = self.screen_rect.centery
            self.rect.left = self.screen_rect.left
        elif orientation == "Right":
            self.rect.centery = self.screen_rect.centery
            self.rect.right = self.screen_rect.right
        elif orientation == "Bottom":
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom

    def fillme(self):
        self.screen.fill(self.paddle_color, self.rect)
