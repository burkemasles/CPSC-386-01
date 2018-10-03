import pygame
import sys
from pygame.sprite import Group
import time


def update_screen(settings, screen, paddle_right, paddle_left, paddle_bottom, ball, enemy, sb):
    screen.fill(settings.bg_color)
    sb.show_score()
    paddle_left.fillme()
    paddle_right.fillme()
    paddle_bottom.fillme()
    ball.fillme()
    enemy.fillme()
    pygame.display.flip()


def check_events(settings, screen, paddle_left, paddle_right, paddle_bottom, play_button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_keydown_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom):
    if event.key == pygame.K_RIGHT:
        paddle_bottom.bottom_right = True
    elif event.key == pygame.K_LEFT:
        paddle_bottom.bottom_left = True
    elif event.key == pygame.K_UP:
        paddle_right.right_up = True
    elif event.key == pygame.K_DOWN:
        paddle_right.right_down = True
    elif event.key == pygame.K_w:
        paddle_left.left_up = True
    elif event.key == pygame.K_s:
        paddle_left.left_down = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom):
    if event.key == pygame.K_RIGHT:
        paddle_bottom.bottom_right = False
    elif event.key == pygame.K_LEFT:
        paddle_bottom.bottom_left = False
    elif event.key == pygame.K_UP:
        paddle_right.right_up = False
    elif event.key == pygame.K_DOWN:
        paddle_right.right_down = False
    elif event.key == pygame.K_w:
        paddle_left.left_up = False
    elif event.key == pygame.K_s:
        paddle_left.left_down = False


def check_ball_paddle_collisions(paddle_right, paddle_left, paddle_bottom, ball, enemy):
    paddles = Group()
    paddles.add(paddle_bottom)
    paddles.add(paddle_right)
    paddles.add(paddle_left)
    paddles.add(enemy)
    collision = pygame.sprite.spritecollideany(ball, paddles)

    if collision is not None:
        ball.switch_direction(collision)
        ball.boing.play()


def update_button(play_button):
    play_button.draw_button()
    pygame.display.flip()


def check_play_button(stats, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True