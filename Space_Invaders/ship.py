import pygame
from pygame.sprite import Sprite
from spritesheet import Spritesheet


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initilize the ship and set its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.ss = Spritesheet('images/Ship(2).png')
        self.rectangle = pygame.Rect(0, 0, 24, 24)
        self.image = self.ss.image_at(self.rectangle)
        self.image = pygame.transform.scale2x(self.image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx

    def destroy_ship(self):
        self.rectangle.y += 24
        self.rectangle.w += 24
        self.rectangle.h += 24
        self.image = self.ss.image_at(self.rectangle)
        self.image = pygame.transform.scale2x(self.image)

    def reset_ship(self):
        self.rectangle.y = 0
        self.rectangle.w = 24
        self.rectangle.h = 24
        self.image = self.ss.image_at(self.rectangle)
        self.image = pygame.transform.scale2x(self.image)