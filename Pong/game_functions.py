import pygame
import sys


def update_screen(settings, screen, paddle_right, paddle_left, paddle_bottom):
    screen.fill(settings.bg_color)
    paddle_left.fillme()
    paddle_right.fillme()
    paddle_bottom.fillme()
    pygame.display.flip()


# def check_events(settings, screen, paddle_left, paddle_right, paddle_bottom):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == pygame.KEYDOWN:
#             check_keydown_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom)
#
#         elif event.type == pygame.KEYUP:
#             check_keyup_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom)
#
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             check_play_button(settings, screen, mouse_x, mouse_y)
#
#
# def check_keydown_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom):
#
#
# def check_keyup_events(event, settings, screen, paddle_left, paddle_right, paddle_bottom):
#
#
# def check_play_button(settings, screen, mouse_x, mouse_y):