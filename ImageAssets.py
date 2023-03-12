import pygame

def loadImage(id):
    if id == 1:
        return pygame.image.load("graphics/CityWallpaper.png")
    if id == 2:
        return pygame.image.load("graphics/RuinsWallpaper.png")
    if id == 3:
        return pygame.image.load("graphics/TestLevelCity.png")
    if id == 4:
        return pygame.image.load("graphics/TestLevelRuins.png")