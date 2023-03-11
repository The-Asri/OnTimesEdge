factor = 0.9


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Camera:
    def __init__(self, target=None):
        self.target = target
        if target is not None:
            self.x = target.x
            self.y = target.y
        else:
            self.x = 0
            self.y = 0

    def update(self):
        if self.target is not None:
            dx = self.target.x - self.x
            dy = self.target.y - self.y
            self.x += dx * factor
            self.y += dy * factor
