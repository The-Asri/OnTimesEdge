import pygame

key_left = pygame.K_a
key_right = pygame.K_d
key_up = pygame.K_w
key_down = pygame.K_s
key_jump = pygame.K_SPACE
key_switch = pygame.K_e
key_reset = pygame.K_r
key_escape = pygame.K_ESCAPE
key_fullReset = pygame.K_g

class KeyManager:
    def __init__(self):
        self.key_left = False
        self.key_right = False
        self.key_up = False
        self.key_down = False
        self.key_jump = False
        self.key_switch = False
        self.key_reset = False
        self.key_escape = False
        self.key_fullReset = False

    def keyDown(self, key):
        if key == key_left:
            self.key_left = True
        if key == key_right:
            self.key_right = True
        if key == key_up:
            self.key_up = True
        if key == key_down:
            self.key_down = True
        if key == key_jump:
            self.key_jump = True
        if key == key_switch:
            self.key_switch = True
        if key == key_reset:
            self.key_reset = True
        if key == key_escape:
            self.key_escape = True
        if key == key_fullReset:
            self.key_fullReset = True

    def keyUp(self, key):
        if key == key_left:
            self.key_left = False
        if key == key_right:
            self.key_right = False
        if key == key_up:
            self.key_up = False
        if key == key_down:
            self.key_down = False
        if key == key_jump:
            self.key_jump = False
        if key == key_switch:
            self.key_switch = False
        if key == key_reset:
            self.key_reset = False
        if key == key_escape:
            self.key_escape = False
        if key == key_fullReset:
            self.key_fullReset = False
