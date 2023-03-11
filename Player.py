import box

gravity = 0.6
gravityCap = 0.2
jumpPower = 4
jumpCap = 1.5
speed = 0.5
friction_standing = 0.5
friction_running = 0.85
friction_jumping = 0.99
jumpSpeedBoost = 1.25
jumpBoost = 1.35
jumpStop = 0.85

class Player(box.Box):
    def __init__(self, x, y):
        super().__init__(x, y, 12, 12)
        self.vx = 0
        self.vy = 0

    def update(self, boxes, keyManager):
        if self.onGround(boxes):
            self.vy = 0

            state = "standing"
            if keyManager.key_left and not keyManager.key_right:
                state = "left"
            if not keyManager.key_left and keyManager.key_right:
                state = "right"

            if state == "left":
                self.vx -= speed
                self.vx *= friction_running
            if state == "right":
                self.vx += speed
                self.vx *= friction_running
            if state == "standing":
                self.vx *= friction_standing

            if keyManager.key_jump:
                self.vy -= (jumpPower + abs(self.vx)) / jumpCap

                if state == "left" and self.vx > 0:
                    self.vx *= jumpStop
                    self.vy -= abs(self.vx) * jumpBoost
                elif state == "right" and self.vx < 0:
                    self.vx *= jumpStop
                    self.vy -= abs(self.vx) * jumpBoost
                else:
                    self.vx *= jumpSpeedBoost

        else:
            self.vx *= friction_jumping

        self.vy += gravity
        if keyManager.key_jump:
            self.vy -= gravityCap

        self.moveX(boxes)
        self.moveY(boxes)

    def moveX(self, boxes):
        hb = self.getHitbox()
        hb.x += self.vx
        for b in boxes:
            if b.isColliding(hb):
                if self.vx > 0:
                    self.x = b.x - hb.width + 2 - 0.069
                if self.vx < 0:
                    self.x = b.x + b.width + 2 + 0.069
                self.vx = 0
                return
        self.x += self.vx

    def moveY(self, boxes):
        hb = self.getHitbox()
        hb.y += self.vy
        for b in boxes:
            if b.isColliding(hb):
                if self.vy > 0:
                    self.y = b.y - hb.height - 0.069
                if self.vy < 0:
                    self.y = b.y + b.height + 0.069
                self.vy = 0
                return
        self.y += self.vy


    def draw(self, s, c):
        self.getHitbox().draw(s, c)


    def getHitbox(self):
        return box.Box(self.x - 2, self.y, 8, 12)


    def onGround(self, boxes):
        hb = self.getHitbox()
        hb.y += 1
        for b in boxes:
            if b.isColliding(hb):
                return True
        return False
