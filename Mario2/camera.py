from pygame import *


class Camera:
    def __init__(self, platforms):
        self.background_x = 0
        self.platforms = platforms
        self.edge = Rect(700, 0, 20, 2000)

    def update(self, speed):
        self.background_x -= int(speed)
        for p in self.platforms:
            p.x -= int(speed)