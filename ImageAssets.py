import pygame

def loadImage(id):
    if id == 1:
        return pygame.image.load("graphics/CityWallpaper.png")
    if id == 2:
        return pygame.image.load("graphics/RuinsWallpaper.png")
    if id == 7:
        return pygame.image.load("graphics/CityLevel3.png")
    if id == 8:
        return pygame.image.load("graphics/RuinsLevel3.png")
    if id == 9:
        return pygame.image.load("graphics/Player.png")