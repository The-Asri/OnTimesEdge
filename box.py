import pygame.surface


class Box:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def getPoints(self):
        return [[self.x - self.width/2, self.y - self.height/2], [self.x + self.width/2, self.y - self.height/2],
                [self.x - self.width/2, self.y + self.height/2], [self.x + self.width/2, self.y + self.height/2]]

    def draw(self, s, c):
        pygame.draw.rect(s, "Red", (self.x - self.width/2 - c.x, self.y - self.height/2 - c.y, self.width, self.height), 1)

    def is_colliding(self, b):
        for point in b.getPoints():
            if self.x - self.width / 2 <= point[0] <= self.x + self.width / 2 and \
                    self.y - self.height / 2 <= point[1] <= self.y + self.height / 2:
                return True
        return False
