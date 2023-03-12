import pygame

def loadImage(id):
    if id == 1:
        return pygame.image.load("graphics/TestLevelCity.png")
    if id == 2:
        return pygame.image.load("graphics/TestLevelRuins.png")