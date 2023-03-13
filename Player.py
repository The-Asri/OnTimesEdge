import pygame
import box

gravity = 0.6
gravityCap = 0.2
jumpPower = 4
jumpCap = 1.5
speed = 0.5
arialSpeed = 0.1
friction_standing = 0.6
friction_running = 0.85
friction_jumping = 0.95
jumpSpeedBoost = 1.25
jumpBoost = 1.2
jumpStop = 1.1
wallJumpPower = 4


class Player(box.Box):
    def __init__(self, x, y):
        super().__init__(x, y, 12, 12)
        self.vx = 0
        self.vy = 0
        self.direction = "right"
        self.sliding = False
        self.jumpLock = False
        self.isDead = False

    def update(self, boxes, keyManager):
        if not keyManager.key_jump:
            self.jumpLock = False

        state = "standing"
        if keyManager.key_left and not keyManager.key_right:
            state = "left"
        if not keyManager.key_left and keyManager.key_right:
            state = "right"

        if self.onGround(boxes):
            if self.sliding:
                self.sliding = False

            self.vy = 0

            if state == "left":
                self.vx -= speed
                self.vx *= friction_running
            if state == "right":
                self.vx += speed
                self.vx *= friction_running
            if state == "standing":
                self.vx *= friction_standing

            if keyManager.key_jump and not self.jumpLock:
                self.jumpLock = True
                self.vy -= (jumpPower + abs(self.vx)) / jumpCap

                if state == "left" and self.vx > 0:
                    self.vy -= abs(self.vx) * jumpBoost
                    self.vx *= jumpStop
                elif state == "right" and self.vx < 0:
                    self.vy -= abs(self.vx) * jumpBoost
                    self.vx *= jumpStop
                else:
                    self.vx *= jumpSpeedBoost
        else:
            self.vx *= friction_jumping
            if state == "left":
                self.vx -= arialSpeed
            if state == "right":
                self.vx += arialSpeed

            if self.onWall(boxes):
                self.sliding = True
                self.moveX(boxes)

        if self.sliding:
            self.vy = min(gravity, self.vy + gravity)
            if not self.onWall(boxes):
                self.sliding = False
            if self.direction != state:
                self.sliding = False
            if keyManager.key_jump and not self.jumpLock:
                self.jumpLock = True
                if self.direction == "right":
                    self.vx -= wallJumpPower
                if self.direction == "left":
                    self.vx += wallJumpPower
                self.vy -= jumpPower
                self.sliding = False
        else:
            self.vy += gravity
            if keyManager.key_jump:
                self.vy -= gravityCap

        if self.vx > 0:
            self.direction = "right"
        if self.vx < 0:
            self.direction = "left"

        self.moveX(boxes)
        self.moveY(boxes)

    def moveX(self, boxes):
        hb = self.getHitbox()
        hb.x += self.vx
        for b in boxes:
            if b.isColliding(hb):
                if b.type == "Spike":
                    self.isDead = True
                if self.vx > 0:
                    self.x = b.x - hb.width - 2 - 0.069
                if self.vx < 0:
                    self.x = b.x + b.width - 2 + 0.069
                self.vx = 0
                return
        self.x += self.vx

    def moveY(self, boxes):
        hb = self.getHitbox()
        hb.y += self.vy
        for b in boxes:
            if b.isColliding(hb):
                if b.type == "Spike":
                    self.isDead = True
                if self.vy > 0:
                    self.y = b.y - hb.height - 0.069
                if self.vy < 0:
                    self.y = b.y + b.height + 0.069
                self.vy = 0
                return
        self.y += self.vy


    def draw(self, s, c):
        hb = self.getHitbox()
        hb.width += 1
        hb.height += 1
        hb.draw(s, c)
        #pygame.draw.rect(s, "Red", (self.x - c.x, self.y - c.y, self.width, self.height), 1)


    def getHitbox(self):
        return box.Box(self.x + 2, self.y, 8, 12)

    def onGround(self, boxes):
        hb = self.getHitbox()
        hb.y += 1
        for b in boxes:
            if b.isColliding(hb) and b.type != "Spike":
                return True
        return False

    def onWall(self, boxes):
        hb = self.getHitbox()
        if self.sliding:
            if self.direction == "right":
                hb.x += 1
            if self.direction == "left":
                hb.x -= 1
        else:
            hb.x += self.vx
        for b in boxes:
            if b.isColliding(hb) and b.type == "Normal":
                return True
        return False
