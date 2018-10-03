import pygame
from pygame.sprite import Sprite
from paddle import Paddle
from enemy_paddle import Enemy
from random import randint


class Ball(Sprite):
    def __init__(self, settings, screen, stats, sb):
        super(Ball, self).__init__()
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.sb = sb
        self.screen_rect = screen.get_rect()
        self.ball_color = (255, 255, 255)

        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect.center = self.screen_rect.center

        self.reset_ball()
        self.dx = 0.4
        self.dy = 0.4

        self.boing = pygame.mixer.Sound("boing.wav")

    def fillme(self):
        self.screen.fill(self.ball_color, self.rect)

    def update(self, stats, sb):
        if self.moving_right:
            self.posx += self.dx
            self.rect.centerx = self.posx
        elif self.moving_left:
            self.posx -= self.dx
            self.rect.centerx = self.posx
        if self.moving_up:
            self.posy -= self.dy
            self.rect.centery = self.posy
        elif self.moving_down:
            self.posy += self.dy
            self.rect.centery = self.posy

        if self.rect.right > self.screen_rect.right or self.rect.left < 0 or self.rect.top < 0 or self.rect.bottom > self.screen_rect.bottom:
            stats.score += 1
            sb.prep_score()
            self.reset_ball()


    def switch_direction(self, paddle):
        if type(paddle) is Paddle:
            if paddle.orientation == "Left":
                if self.rect.centery <= paddle.rect.centery:
                    self.moving_up = True
                    self.moving_down = False
                    self.moving_right = True
                    self.moving_left = False
                elif self.rect.centery > paddle.rect.centery:
                    self.moving_up = False
                    self.moving_down = True
                    self.moving_right = True
                    self.moving_left = False
            elif paddle.orientation == "Right":
                if self.rect.centery <= paddle.rect.centery:
                    self.moving_up = True
                    self.moving_down = False
                    self.moving_right = False
                    self.moving_left = True
                elif self.rect.centery > paddle.rect.centery:
                    self.moving_up = False
                    self.moving_down = True
                    self.moving_right = False
                    self.moving_left = True
            else:
                if self.rect.centerx <= paddle.rect.centerx:
                    self.moving_right = False
                    self.moving_left = True
                    self.moving_down = False
                    self.moving_up = True
                elif self.rect.centerx > paddle.rect.centerx:
                    self.moving_right = True
                    self.moving_left = False
                    self.moving_down = False
                    self.moving_up = True

        if type(paddle) is Enemy:
            num = randint(0, 1)
            if num == 0:
                self.moving_right = False
                self.moving_left = True
                self.moving_down = True
                self.moving_up = False
            elif num == 1:
                self.moving_right = True
                self.moving_left = False
                self.moving_down = True
                self.moving_up = False

        # if self.moving_right:
        #     self.moving_right = False
        # else:
        #     self.moving_right = True
        # if self.moving_left:
        #     self.moving_left = False
        # else:
        #     self.moving_left = True
        # if self.moving_down:
        #     self.moving_down = False
        # else:
        #     self.moving_down = True
        # if self.moving_up:
        #     self.moving_up = False
        # else:
        #     self.moving_up = True

    def reset_ball(self):
        if self.stats.score >= 5:
            self.stats.game_active = False
            self.sb.prep_gameover()
        else:
            self.rect.center = self.screen_rect.center
            self.posx = self.rect.centerx
            self.posy = self.rect.centery

            num1 = randint(0, 1)
            num2 = randint(2, 3)

            if num1 == 0:
                self.moving_right = True
                self.moving_left = False
            else:
                self.moving_right = False
                self.moving_left = True

            if num2 == 2:
                self.moving_up = True
                self.moving_down = False
            else:
                self.moving_up = False
                self.moving_down = True
