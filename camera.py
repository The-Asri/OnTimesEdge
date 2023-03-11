factor = 0.9


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Camera:
    def __init__(self, target=None):
        self.target = target
        self.x = target.x
        self.y = target.y

    def update(self):
        if self.target is not None:
            dx = self.target.x - self.x
            dy = self.target.y - self.y
            self.x += dx * factor
            self.y += dy * factor
