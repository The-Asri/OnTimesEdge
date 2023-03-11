import box

gravity = 0.6
gravityCap = 0.2
jumpPower = 5
jumpCap = 1.8
speed = 0.5
friction_standing = 0.5
friction_running = 0.85
friction_jumping = 0.99
jumpBoost = 1.15
class Player(box.Box):
    def __init__(self, x, y):
        super().__init__(x, y, 12, 12)
        self.vx = 0
        self.vy = 0

    def update(self, boxes, keyManager):
        if self.onGround(boxes):
            self.vy = 0
            if keyManager.key_left:
                self.vx -= speed
                self.vx *= friction_running
            if keyManager.key_right:
                self.vx += speed
                self.vx *= friction_running
            if not keyManager.key_left and not keyManager.key_right:
                self.vx *= friction_standing
            if keyManager.key_jump:
                self.vy -= (jumpPower + abs(self.vx)) / jumpCap
                self.vx *= jumpBoost
        else:
            self.vx *= friction_jumping

        self.vy += gravity
        if keyManager.key_jump:
            self.vy -= gravityCap

        self.moveY(boxes)
        self.moveX(boxes)

    def moveX(self, boxes):
        hb = self.getHitbox()
        hb.x += self.vx
        for b in boxes:
            if b.isColliding(hb):
                if self.vx > 0:
                    self.x = b.x - b.width/2 - self.width/2 - 0.069
                if self.vx < 0:
                    self.x = b.x + b.width/2 + self.width/2 + 1.069
                self.vx = 0
                return
        self.x += self.vx

    def moveY(self, boxes):
        hb = self.getHitbox()
        hb.y += self.vy
        for b in boxes:
            if b.isColliding(hb):
                if self.vy > 0:
                    self.y = b.y - b.height/2 - self.height/2 - 0.069
                if self.vy < 0:
                    self.y = b.y + b.height/2 + self.height/2 + 1.069
                self.vy = 0
                return
        self.y += self.vy
    def draw(self, s, c):
        self.getHitbox().draw(s, c)

    def getHitbox(self):
        return box.Box(self.x, self.y, 8, 12)
    def onGround(self, boxes):
        hb = self.getHitbox()
        hb.y += 1
        for b in boxes:
            if b.isColliding(hb):
                return True
        return False
