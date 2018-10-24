import pygame
import pygame.sprite
from character import Character


class Pacman(Character):
    def __init__(self, sheet_location, pos, screen, map):
        super().__init__(sheet_location, pos, screen, map)

    def update(self, pacman_timer):
        timer_image = pacman_timer.imagerect()
        if self.velocity == (1, 0):
            if pacman_timer.frameindex == 3:
                pacman_timer.frameindex = 0
            else:
                self.image = timer_image
        elif self.velocity == (-1, 0):
            if pacman_timer.frameindex == 1:
                pacman_timer.frameindex = 3
            elif pacman_timer.frameindex == 5:
                pacman_timer.frameindex = 0
            else:
                self.image = timer_image
        elif self.velocity == (0, -1):
            if pacman_timer.frameindex == 1:
                pacman_timer.frameindex = 5
            elif pacman_timer.frameindex == 7:
                pacman_timer.frameindex = 0
            else:
                self.image = timer_image
        elif self.velocity == (0, 1):
            if pacman_timer.frameindex == 1:
                pacman_timer.frameindex = 7
            elif pacman_timer.frameindex == 9:
                pacman_timer.frameindex = 0
            else:
                self.image = timer_image
        elif self.velocity == (0, 0):
            pacman_timer.frameindex = 0
        else:
            self.image = timer_image