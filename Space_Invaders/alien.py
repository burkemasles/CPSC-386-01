import pygame
from pygame.sprite import Sprite
from spritesheet import Spritesheet


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen, alien_type):
        """Initialize the alien and set its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.alien_type = alien_type
        self.sprite_number = 0

        if self.alien_type == 0:
            self.ss = Spritesheet('images/Big AlienV2.png')
            self.image = self.ss.image_at((0, 0, 35, 24))
        elif self.alien_type == 1:
            self.ss = Spritesheet('images/Medium AlienV6.png')
            self.image = self.ss.image_at((0, 0, 35, 24))
        elif self.alien_type == 2:
            self.ss = Spritesheet('images/Small AlienV2.png')
            self.image = self.ss.image_at((0, 0, 35, 24))

        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien left of right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def change_sprite(self):
        if self.sprite_number == 0:
            self.image = self.ss.image_at((0, 24, 70, 48))
            self.sprite_number = 1
        elif self.sprite_number == 1:
            self.image = self.ss.image_at((0, 0, 35, 24))
            self.sprite_number = 0
        self.image = pygame.transform.scale2x(self.image)
