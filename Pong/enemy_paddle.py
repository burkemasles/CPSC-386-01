import pygame
from pygame.sprite import Sprite
import threading


class Enemy(Sprite):
    def __init__(self, settings, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.paddle_color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 100, 10)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

    def fillme(self):
        self.screen.fill(self.paddle_color, self.rect)

    def follow_ball(self, ball):
        if self.rect.centerx < ball.rect.centerx and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.rect.centerx > ball.rect.centerx and self.rect.left > 0:
            self.rect.centerx -= 1

    # def follow_ball(self, ball):
    #     threading.Timer(1.0, self.follow_ball).start()
    #     if self.rect.centerx < ball.rect.centerx and self.rect.right < self.screen_rect.right:
    #         self.rect.centerx += 1
    #     elif self.rect.centerx > ball.rect.centerx and self.rect.left > 0:
    #         self.rect.centerx -= 1
    #     self.follow_ball(ball)