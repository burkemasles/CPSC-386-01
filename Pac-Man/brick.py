from imagerect import ImageRect
from pygame.sprite import Sprite


class Brick(Sprite):
    def __init__(self, screen):
        super(Brick, self).__init__()
        self.image_rect = ImageRect(screen, 'images/Block.png', 34, 34)
        self.image = self.image_rect.image
        self.rect = self.image_rect.rect

    def blitme(self):
        self.screen.blit(self.image_rect.image, self.image_rect.rect)