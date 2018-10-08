import pygame

class Spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert_alpha()
        image.fill((0, 0, 0, 0))
        image.blit(self.sheet, (0, 0), rect)
        return image

# Saw this online, looks way better but is it plagiarism????
# def strip_from_sheet(sheet, start, size, columns, rows):
#     frames = []  #This is the group of frames in the image
#     for j in range(rows):  #For each row (goes down then over)
#         for i in range(columns):  #For each column
#             location = (start[0]+size[0]*i, start[1]+size[1]*j)
#             frames.append(sheet.subsurface(pg.Rect(location, size)))
#     return frames