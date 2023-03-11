factor = 0.2


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Camera:
    def __init__(self, w, h, target=None):
        self.target = target
        if target is not None:
            self.x = target.x - w / 2
            self.y = target.y - h / 2
        else:
            self.x = w / 2
            self.y = h / 2

    def update(self, w, h):
        if self.target is not None:
            dx = self.target.x - self.x - w / 2
            dy = self.target.y - self.y - h / 2
            self.x += dx * factor
            self.y += dy * factor
