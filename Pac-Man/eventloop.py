import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    @staticmethod
    def check_events(pacman, pacman_timer):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_RIGHT:
                    pacman.change_direction('r', pacman_timer)
                elif event.key == pygame.K_LEFT:
                    pacman.change_direction('l', pacman_timer)
                elif event.key == pygame.K_UP:
                    pacman.change_direction('u', pacman_timer)
                elif event.key == pygame.K_DOWN:
                    pacman.change_direction('d', pacman_timer)