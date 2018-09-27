import pygame
from settings import Settings
import game_functions as gf
from paddle import Paddle


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    pygame.display.set_caption("Pong!")
    paddle_left, paddle_right, paddle_bottom = Paddle(settings, screen, "Left"), Paddle(settings, screen, "Right"), Paddle(settings, screen, "Bottom")

    while True:
        gf.update_screen(settings, screen, paddle_left, paddle_right, paddle_bottom)


run_game()
