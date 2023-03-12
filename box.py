import pygame.surface


class Box:
    def __init__(self, x, y, w, h, type="Normal"):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.type = type

    def getPoints(self):
        return [[self.x, self.y], [self.x + self.width, self.y],
                [self.x, self.y + self.height], [self.x + self.width, self.y + self.height]]

    def draw(self, s, c):
        pygame.draw.rect(s, "Red", (int(self.x) - c.x, int(self.y) - c.y, self.width, self.height), 1)

    def isColliding(self, b):
        for point in b.getPoints():
            if self.x <= point[0] and point[0] <= self.x + self.width and self.y <= point[1] and point[1] <= self.y + self.height:
                return True
        return False
