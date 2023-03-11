

class Border:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self, x, maxX):
        if x < 0 and maxX > self.x:
            return (x + maxX) / 2
        if x < 0:
            return 0
        if maxX > self.x:
            return self.x - (maxX - x)
        return x

    def getY(self, y, maxY):
        if y < 0 and maxY > self.y:
            return (y + maxY) / 2
        if y < 0:
            return 0
        if maxY > self.y:
            return self.y - (maxY - y)
        return y
