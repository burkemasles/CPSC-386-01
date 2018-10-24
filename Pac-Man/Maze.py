import pygame
from imagerect import ImageRect
from brick import Brick
from food import Food
from pygame import mixer


class Maze:
    def __init__(self, screen, file_name):
        self.screen = screen
        with open(file_name, 'r') as file:
            self.rows = file.readlines()
        self.foods = []
        n = 22
        m = 25
        self.empty_space = [[0] * n for i in range(m)]
        self.empty_space[24][21] = pygame.Rect(5, 5, 5, 5)
        self.empty_space_dict = {}
        self.bricks = []
        self.map = []
        self.food = Food(screen)
        self.brick = Brick(screen)
        self.deltax = self.deltay = 34
        self.pacman_pos = (0, 0)
        self.red_pos = (0, 0)
        self.orange_pos = (0, 0)
        self.graph = {}
        self.chomp_start = pygame.mixer.Sound("images/pacman_chomp1.wav")
        self.chomp_end = pygame.mixer.Sound("images/pacman_chomp2.wav")
        self.chomp = 0

        self.build()

    def build(self):
        r = self.brick.image_rect.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay
        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            self.map.append(row)
            for ncol in range(len(row)):
                col = row[ncol]
                self.empty_space[nrow][ncol] = pygame.Rect(ncol * dx, nrow * dy, w, h)
                if col == 'x':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'p':
                    self.pacman_pos = (ncol * dx, (nrow * dy) + 3)
                elif col == 'r':
                    self.red_pos = (ncol * dx, (nrow * dy) + 3)
                    row1 = self.rows[nrow - 1]
                    row2 = self.rows[nrow + 1]
                    self.graph[str(chr(96 + nrow)) + str(ncol)] = {}
                    if row1[ncol] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow - 1)) + str(ncol)] = 1
                    if row2[ncol] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow + 1)) + str(ncol)] = 1
                    if row[ncol - 1] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow)) + str(ncol - 1)] = 1
                    if row[ncol + 1] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow)) + str(ncol + 1)] = 1
                elif col == 'o':
                    self.orange_pos = (ncol * dx, (nrow * dy) + 3)
                elif col == ' ':
                    self.foods.append(pygame.Rect(ncol * dx + 14, nrow * dy + 14, w - 14, h - 14))
                    # self.empty_space[nrow][ncol] = pygame.Rect(ncol * dx + 14, nrow * dy + 14, w - 14, h - 14)
                    row1 = self.rows[nrow - 1]
                    row2 = self.rows[nrow + 1]
                    self.graph[str(chr(96 + nrow)) + str(ncol)] = {}
                    if row1[ncol] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow - 1)) + str(ncol)] = 1
                    if row2[ncol] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow + 1)) + str(ncol)] = 1
                    if row[ncol - 1] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow)) + str(ncol - 1)] = 1
                    if row[ncol + 1] == ' ':
                        self.graph[str(chr(96 + nrow)) + str(ncol)][str(chr(96 + nrow)) + str(ncol + 1)] = 1
        for i in range(len(self.empty_space)):
            row = self.empty_space[i]
            for j in range(len(row)):
                x = row[j]
                self.empty_space_dict[tuple(x)] = str(chr(97 + i)) + str(j)

    def build_group(self, bricks, foods):
        for rect in self.bricks:
            brick = Brick(self.screen)
            brick.rect = rect
            bricks.add(brick)
        for rect1 in self.foods:
            food = Food(self.screen)
            food.rect = rect1
            foods.add(food)

    def wall_collide(self, bricks, sprite):
        return pygame.sprite.spritecollideany(sprite, bricks)

    def food_collide(self, foods, sprite):
        collision = pygame.sprite.spritecollideany(sprite, foods)
        if collision is not None:
            foods.remove(collision)
            self.foods.remove(collision.rect)
            if self.chomp == 0:
                self.chomp_start.play()
                self.chomp = 1
            elif self.chomp == 1:
                self.chomp_end.play()
                self.chomp = 0

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image_rect.image, rect)
        for rect in self.foods:
            self.screen.blit(self.food.image_rect.image, rect)
        # self.file = open(file_name, 'r')
        # self.line = ""
        # while self.file:
        #     self.line = self.file.readline()
        #     if self.line == '':
        # self.brick.rect = pygame.Rect(ncol * dx, nrow * dy, w, h)
        #            self.brickss.add(self.brick)
