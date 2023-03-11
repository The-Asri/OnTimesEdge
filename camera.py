factor = 0.25


class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Camera:
    def __init__(self, w, h, border, target=None):
        self.target = target
        if target is not None:
            x = target.x - w / 2
            y = target.y - h / 2
            self.x = border.getX(x, x + w)
            self.y = border.getY(y, y + h)
        else:
            self.x = border.getX(0, w)
            self.y = border.getX(0, h)

    def update(self, w, h, border):
        if self.target is not None:
            dx = self.target.x - self.x - w / 2
            dy = self.target.y - self.y - h / 2
            self.x += dx * factor
            self.y += dy * factor
            self.x = border.getX(self.x, self.x + w)
            self.y = border.getY(self.y, self.y + h)
