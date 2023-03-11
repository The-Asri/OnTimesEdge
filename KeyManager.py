import pygame


class KeyManager:
    def __init__(self):
        self.key_left = False
        self.key_right = False
        self.key_jump = False
        self.key_switch = False
        self.key_reset = False
        self.key_escape = False

    def keyDown(self, key):
        if key == pygame.K_a:
            self.key_left = True
        if key == pygame.K_d:
            self.key_right = True
        if key == pygame.K_SPACE:
            self.key_jump = True
        if key == pygame.K_e:
            self.key_switch = True
        if key == pygame.K_r:
            self.key_reset = True
        if key == pygame.K_ESCAPE:
            self.key_escape = True

    def keyUp(self, key):
        if key == pygame.K_a:
            self.key_left = False
        if key == pygame.K_d:
            self.key_right = False
        if key == pygame.K_SPACE:
            self.key_jump = False
        if key == pygame.K_e:
            self.key_switch = False
        if key == pygame.K_r:
            self.key_reset = False
        if key == pygame.K_ESCAPE:
            self.key_escape = False


