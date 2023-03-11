import pygame
from sys import exit


def eventHandler(keyManager):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            keyManager.keyDown(event.key)
        if event.type == pygame.KEYUP:
            keyManager.keyUp(event.key)

