import pygame
from pygame.sprite import Sprite


class Paddle(Sprite):
    def __init__(self, settings, screen, orientation):
        super(Paddle, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.orientation = orientation
        if self.orientation == "Bottom":
            self.width, self.height = 100, 10
        elif self.orientation == "Left" or "Right":
            self.width, self.height = 10, 100
        self.paddle_color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.bottom_right = False
        self.bottom_left = False
        self.right_up = False
        self.right_down = False
        self.left_up = False
        self.left_down = False
        if self.orientation == "Left":
            self.rect.centery = self.screen_rect.centery
            self.rect.left = self.screen_rect.left
        elif self.orientation == "Right":
            self.rect.centery = self.screen_rect.centery
            self.rect.right = self.screen_rect.right
        elif self.orientation == "Bottom":
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom

    def fillme(self):
        self.screen.fill(self.paddle_color, self.rect)

    def update_bottom(self):
        if self.bottom_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.bottom_left and self.rect.left > 0:
            self.rect.centerx -= 1

    def update_left(self):
        if self.left_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        elif self.left_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def update_right(self):
        if self.right_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        elif self.right_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1
