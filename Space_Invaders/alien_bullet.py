import pygame
from pygame.sprite import Sprite


class Alien_Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet object at the ship's current position"""
        super(Alien_Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.centery

        self.y = float(self.rect.y)

        self.color = (255, 0, 0)
        self.speed_factor = 1

    def update(self):
        """Move the bullet up the screen"""
        self.y += self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)