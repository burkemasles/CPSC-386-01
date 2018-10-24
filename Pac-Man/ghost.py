import pygame
from pygame.sprite import Sprite
from dijkstra import dijkstra


class Ghost(Sprite):
    def __init__(self, type, pos, screen, sheet_location):
        super(Ghost, self).__init__()
        self.screen = screen
        self.type = type
        self.pos = pos
        self.current_pos = 'k10'
        self.sheet = pygame.image.load(sheet_location).convert_alpha()
        self.rect = pygame.Rect(pos[0], pos[1], 28, 26)
        self.speed_counter = 0
        self.current_index = 1
        self.path = []
        self.moving_x = False
        self.moving_y = True
        self.both_ways = 0
        self.direction = ''
        self.finished = False

    def strip_from_sheet(self, start, size, columns, rows):
        frames = []  # This is the group of frames in the image
        for j in range(rows):  # For each row (goes down then over)
            for i in range(columns):  # For each column
                location = (start[0] + size[0] * i, start[1] + size[1] * j)
                frames.append(self.sheet.subsurface(pygame.Rect(location, size)))
        return frames

    def set_image(self, image):
        self.image = image

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, pacman_pos, graph):
        self.path = dijkstra(graph, self.current_pos, pacman_pos)
        if len(self.path) == 1:
            self.current_index = 0
        self.finished = False

    def update_image(self, ghost_timer):
        timer_image = ghost_timer.imagerect()
        if self.direction == 'r':
            if ghost_timer.frameindex == 2:
                ghost_timer.frameindex = 0
            else:
                self.image = timer_image
        elif self.direction == 'l':
            if ghost_timer.frameindex == 4:
                ghost_timer.frameindex = 2
            else:
                self.image = timer_image
        elif self.direction == 'u':
            if ghost_timer.frameindex == 6:
                ghost_timer.frameindex = 4
            else:
                self.image = timer_image
        elif self.direction == 'd':
            if ghost_timer.frameindex == 0:
                ghost_timer.frameindex = 6
            else:
                self.image = timer_image

    def update_movement(self, empty_space, ghost_timer):
        if self.speed_counter == 3:
            self.speed_counter = 0
            if self.moving_x:
                if self.rect.centerx > empty_space[
                        ord(self.path[self.current_index][0]) - 96][int(self.path[self.current_index][1:3])].centerx:
                    self.rect.centerx -= 1
                    if self.direction != 'l':
                        ghost_timer.frameindex = 2
                    self.direction = 'l'
                elif self.rect.centerx < empty_space[
                        ord(self.path[self.current_index][0]) - 96][int(self.path[self.current_index][1:3])].centerx:
                    self.rect.centerx += 1
                    if self.direction != 'r':
                        ghost_timer.frameindex = 0
                    self.direction = 'r'
                else:
                    self.moving_y = True
                    self.moving_x = False
                    self.both_ways += 1
            elif self.moving_y:
                if self.rect.centery > empty_space[
                        ord(self.path[self.current_index][0]) - 96][int(self.path[self.current_index][1:3])].centery:
                    self.rect.centery -= 1
                    if self.direction != 'u':
                        ghost_timer.frameindex = 4
                    self.direction = 'u'
                elif self.rect.centery < empty_space[
                        ord(self.path[self.current_index][0]) - 96][int(self.path[self.current_index][1:3])].centery:
                    self.rect.centery += 1
                    if self.direction != 'd':
                        ghost_timer.frameindex = 6
                    self.direction = 'd'
                else:
                    self.moving_y = False
                    self.moving_x = True
                    self.both_ways += 1
            if self.both_ways >= 2:
                self.both_ways = 0
                if self.current_index != len(self.path) - 1:
                    self.current_index += 1
                else:
                    self.moving_y = False
                    self.moving_x = False
                    self.both_ways = 0
        else:
            self.speed_counter += 1
        if self.current_index == len(self.path) - 1:
            self.current_pos = self.path[self.current_index]
            self.current_index = 1
            self.finished = True
# foods[122 - ord(self.path[self.current_index][0])][self.path[self.current_index][1:3]]
