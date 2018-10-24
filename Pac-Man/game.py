import pygame
from Maze import Maze
from eventloop import EventLoop
from timer import Timer
from pygame.sprite import Group
from pacman import Pacman
from ghost import Ghost
import random
from dijkstra import dijkstra


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((714, 900))
        pygame.display.set_caption("Pac-Man")
        self.maze = Maze(self.screen, 'images/Maze.txt')
        self.bricks = Group()
        self.foods = Group()
        self.maze.build_group(self.bricks, self.foods)
        self.pacman = Pacman('images/Pac-Man1.png', self.maze.pacman_pos, self.screen, self.maze.map)
        self.red = Ghost('red', self.maze.red_pos, self.screen, 'images/Red.png')
        self.red_timer = Timer(self.red.strip_from_sheet((0, 0), (28, 26), 8, 1))
        self.red.set_image(self.red_timer.imagerect())
        self.orange = Ghost('orange', self.maze.orange_pos, self.screen, 'images/orange.png')
        self.orange_timer = Timer(self.orange.strip_from_sheet((0, 0), (28, 26), 8, 1))
        self.orange.set_image(self.orange_timer.imagerect())
        self.pacman_timer = Timer(self.pacman.strip_from_sheet((0, 0), (28, 28), 9, 1))
        self.pacman.set_image(self.pacman_timer.imagerect())
        self.graph = self.maze.graph.copy()
        self.red.update('w19', self.graph)
        self.orange.update('a1', self.graph)

    def play(self):
        event_loop = EventLoop(False)

        while not event_loop.finished:
            event_loop.check_events(self.pacman, self.pacman_timer)
            self.maze.food_collide(self.foods, self.pacman)
            self.red.update_movement(self.maze.empty_space, self.red_timer)
            self.orange.update_movement(self.maze.empty_space, self.orange_timer)
            # self.pacman.rect.collidedict(self.maze.empty_space_dict)[1]
            self.red.update_image(self.red_timer)
            self.orange.update_image(self.orange_timer)
            if self.red.finished:
                new_red = random.choice(list(self.graph))
                if new_red != self.red.current_pos:
                    self.red.update(random.choice(list(self.graph)), self.graph)
            if self.orange.finished:
                new_orange = random.choice(list(self.graph))
                if new_orange != self.orange.current_pos:
                    self.orange.update(random.choice(list(self.graph)), self.graph)
            self.update_screen()

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.maze.blitme()
        self.pacman.update_movement(self.maze.wall_collide(self.bricks, self.pacman))
        self.pacman.update(self.pacman_timer)
        self.red.blitme()
        self.orange.blitme()
        self.pacman.blitme()
        pygame.display.flip()

    def strip_from_sheet(self, sheet, start, size, columns, rows):
        frames = []  # This is the group of frames in the image
        for j in range(rows):  # For each row (goes down then over)
            for i in range(columns):  # For each column
                location = (start[0] + size[0] * i, start[1] + size[1] * j)
                frames.append(sheet.subsurface(pygame.Rect(location, size)))
        return frames


game = Game()
game.play()

# character class which gets inherited by pac-man and the ghosts
# pos = velocity (which can be (1,0,0) for left etc)
# ghosts use djikstra
# have timer that gets called, returns the same frame until an amount of time has gone by
