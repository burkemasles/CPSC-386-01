import pygame
from settings import Settings
import game_functions as gf
from paddle import Paddle
from ball import Ball
from enemy_paddle import Enemy
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    pygame.display.set_caption("Pong!")
    paddle_left, paddle_right, paddle_bottom = Paddle(settings, screen, "Left"), \
                                               Paddle(settings, screen, "Right"), Paddle(settings, screen, "Bottom")
    ball = Ball(settings, screen, stats, sb)
    enemy = Enemy(settings, screen)

    play_button = Button(settings, screen)

    while True:
        gf.check_events(settings, screen, paddle_left, paddle_right, paddle_bottom, play_button, stats)
        if stats.game_active:
            ball.update(stats, sb)
            paddle_bottom.update_bottom()
            paddle_right.update_right()
            paddle_left.update_left()
            enemy.follow_ball(ball)
            gf.check_ball_paddle_collisions(paddle_right, paddle_left, paddle_bottom, ball, enemy)
            gf.update_screen(settings, screen, paddle_left, paddle_right, paddle_bottom, ball, enemy, sb)
        else:
            gf.update_button(play_button)


run_game()
