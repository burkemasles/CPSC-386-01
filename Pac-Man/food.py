from imagerect import ImageRect
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen):
        super(Food, self).__init__()
        self.image_rect = ImageRect(screen, 'images/Pill1.png', 3, 3)
        self.image = self.image_rect.image
        self.rect = self.image_rect.rect

    def blitme(self):
        self.screen.blit(self.image_rect.image, self.image_rect.rect)